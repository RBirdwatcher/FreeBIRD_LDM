# coding=UTF-8
# Copyright (c) 2024 Bird Software Solutions Ltd
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License 2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#    Neil Mackenzie - initial API and implementation
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django.db import transaction, connection
from django.conf import settings
from django.views.decorators.http import require_http_methods
from .bird_meta_data_model import (
    VARIABLE_MAPPING, VARIABLE_MAPPING_ITEM, MEMBER_MAPPING, MEMBER_MAPPING_ITEM,
    CUBE_LINK, CUBE_STRUCTURE_ITEM_LINK, MAPPING_TO_CUBE, MAPPING_DEFINITION,
    COMBINATION, COMBINATION_ITEM, CUBE, CUBE_STRUCTURE_ITEM, VARIABLE, MEMBER,
    MAINTENANCE_AGENCY,  MEMBER_HIERARCHY, DOMAIN
)
from . import bird_meta_data_model

from .entry_points.execute_datapoint import RunExecuteDataPoint

import os
import csv
from pathlib import Path

from django.template.loader import render_to_string
from django.db.models import Count, F
from django.views.generic import ListView
from django.urls import reverse
from .context.sdd_context_django import SDDContext
from urllib.parse import unquote
import logging
import zipfile

from django.apps import apps
from django.db import models
import inspect




# Helper function for paginated modelformset views
def paginated_modelformset_view(request, model, template_name, order_by=None):
    # Get all maintenance agencies for the create form
    maintenance_agencies = MAINTENANCE_AGENCY.objects.all().order_by('name')
    
    # Get all member mappings and variable mappings for dropdowns
    member_mappings = MEMBER_MAPPING.objects.all().order_by('name')
    variable_mappings = VARIABLE_MAPPING.objects.all().order_by('name')
    
    # Get paginated formset
    page_number = request.GET.get('page', 1)
    queryset = model.objects.all()
    if order_by:
        queryset = queryset.order_by(order_by)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)
    
    ModelFormSet = modelformset_factory(model, fields='__all__', extra=0)
    
    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, f'{model.__name__} updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, f'There was an error updating the {model.__name__}.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)
    
    context = {
        'formset': formset,
        'page_obj': page_obj,
        'maintenance_agencies': maintenance_agencies,
        'member_mappings': member_mappings,
        'variable_mappings': variable_mappings,
    }
    return render(request, template_name, context)

def show_report(request, report_id):
    return render(request, 'pybirdai/' + report_id)

        


# Basic views
def index(request):
    return HttpResponse("Hello, world. You're at the pybirdai index.")

def home_view(request):
    return render(request, 'pybirdai/home.html')


    return redirect('pybirdai:edit_variable_mapping_items')




# Delete views for various models
def delete_item(request, model, id_field, redirect_view, decoded_id=None):
    try:
        id_value = decoded_id if decoded_id is not None else request.POST.get('id')
        if id_value is None:
            id_value = request.POST.get(id_field)
        item = get_object_or_404(model, **{id_field: id_value})
        item.delete()
        messages.success(request, f'{model.__name__} deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting {model.__name__}: {str(e)}')
    return redirect(f'pybirdai:{redirect_view}')

def delete_variable_mapping(request, variable_mapping_id):
    return delete_item(request, VARIABLE_MAPPING, 'variable_mapping_id', 'edit_variable_mappings', variable_mapping_id)

def execute_data_point(request, data_point_id):
    app_config = RunExecuteDataPoint('pybirdai', 'birds_nest')
    result = app_config.run_execute_data_point(data_point_id)
    
    html_response = f"""

        <h3>DataPoint Execution Results</h3>
        <p><strong>DataPoint ID:</strong> {data_point_id}</p>
        <p><strong>Result:</strong> {result}</p>
        <p><a href="/pybirdai/lineage/">View Lineage Files</a></p>
        <p><a href="/pybirdai/report-templates/">Back to the PyBIRD Reports Templates Page</a></p>
    """
    return HttpResponse(html_response)



def list_lineage_files(request):
    lineage_dir = Path(settings.BASE_DIR) / 'results' / 'lineage'
    csv_files = []
    
    if lineage_dir.exists():
        csv_files = [f.name for f in lineage_dir.glob('*.csv')]
    
    return render(request, 'pybirdai/lineage_files.html', {'csv_files': csv_files})

def view_csv_file(request, filename):

    file_path = Path(settings.BASE_DIR) / 'results' / 'lineage' / filename
    
    if not file_path.exists() or not filename.endswith('.csv'):
        messages.error(request, 'File not found or invalid file type')
        return redirect('pybirdai:list_lineage_files')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)  # Get the headers
            data = list(csv_reader)     # Get all rows
            
        # Paginate the results
        items_per_page = 50  # Adjust this number as needed
        paginator = Paginator(data, items_per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        # Calculate some statistics
        total_rows = len(data)
        num_columns = len(headers)
        
        context = {
            'filename': filename,
            'headers': headers,
            'page_obj': page_obj,
            'total_rows': total_rows,
            'num_columns': num_columns,
            'start_index': (page_obj.number - 1) * items_per_page + 1,
            'end_index': min(page_obj.number * items_per_page, total_rows),
        }
        return render(request, 'pybirdai/view_csv.html', context)
        
    except Exception as e:
        messages.error(request, f'Error reading file: {str(e)}')
        return redirect('pybirdai:list_lineage_files')

def create_response_with_loading(request, task_title, success_message, return_url, return_link_text):
    html_response = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .loading-overlay {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(255, 255, 255, 0.8);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    z-index: 9999;
                }}

                .loading-spinner {{
                    width: 50px;
                    height: 50px;
                    border: 5px solid #f3f3f3;
                    border-top: 5px solid #3498db;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                    margin-bottom: 20px;
                }}

                @keyframes spin {{
                    0% {{ transform: rotate(0deg); }}
                    100% {{ transform: rotate(360deg); }}
                }}

                .loading-message {{
                    font-size: 18px;
                    color: #333;
                }}

                .task-info {{
                    padding: 20px;
                    max-width: 600px;
                    margin: 0 auto;
                }}

                #success-message {{
                    display: none;
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #d4edda;
                    border: 1px solid #c3e6cb;
                    border-radius: 4px;
                    color: #155724;
                }}
            </style>
        </head>
        <body>
            <div class="task-info">
                <h3>{task_title}</h3>
                <div id="loading-overlay" class="loading-overlay">
                    <div class="loading-spinner"></div>
                    <div class="loading-message">Please wait while the task completes...</div>
                </div>
                <div id="success-message">
                    <p>{success_message}</p>
                    <p>Go back to <a href="{return_url}">{return_link_text}</a></p>
                </div>
            </div>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    // Show loading immediately
                    document.getElementById('loading-overlay').style.display = 'flex';
                    document.getElementById('success-message').style.display = 'none';
                    
                    // Start the task execution after a small delay to ensure loading is visible
                    setTimeout(() => {{
                        fetch(window.location.href + '?execute=true', {{
                            method: 'GET',
                            headers: {{
                                'X-Requested-With': 'XMLHttpRequest'
                            }}
                        }})
                        .then(response => response.json())
                        .then(data => {{
                            if (data.status === 'success') {{
                                // Hide loading and show success
                                document.getElementById('loading-overlay').style.display = 'none';
                                document.getElementById('success-message').style.display = 'block';
                            }} else {{
                                throw new Error('Task failed');
                            }}
                        }})
                        .catch(error => {{
                            console.error('Error:', error);
                            alert('An error occurred while processing the task: ' + error.message);
                        }});
                    }}, 100); // Small delay to ensure loading screen is visible
                }});
            </script>
        </body>
        </html>
    """
    
    # If this is the AJAX request to execute the task
    if request.GET.get('execute') == 'true':
        # Execute the actual task
        try:
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return HttpResponse(html_response)


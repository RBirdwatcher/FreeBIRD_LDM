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


from django.contrib import admin


from .bird_meta_data_model import DOMAIN
admin.site.register(DOMAIN)
from .bird_meta_data_model import SUBDOMAIN
admin.site.register(SUBDOMAIN)
from .bird_meta_data_model import FACET_COLLECTION
admin.site.register(FACET_COLLECTION)
from .bird_meta_data_model import MAINTENANCE_AGENCY
admin.site.register(MAINTENANCE_AGENCY)
from .bird_meta_data_model import MEMBER
admin.site.register(MEMBER)
from .bird_meta_data_model import MEMBER_HIERARCHY
admin.site.register(MEMBER_HIERARCHY)
from .bird_meta_data_model import MEMBER_HIERARCHY_NODE
admin.site.register(MEMBER_HIERARCHY_NODE)
from .bird_meta_data_model import VARIABLE
admin.site.register(VARIABLE)
from .bird_meta_data_model import FRAMEWORK
admin.site.register(FRAMEWORK)
from .bird_meta_data_model import MEMBER_MAPPING
admin.site.register(MEMBER_MAPPING)
from .bird_meta_data_model import MEMBER_MAPPING_ITEM
admin.site.register(MEMBER_MAPPING_ITEM)
from .bird_meta_data_model import VARIABLE_MAPPING_ITEM
admin.site.register(VARIABLE_MAPPING_ITEM)
from .bird_meta_data_model import VARIABLE_MAPPING
admin.site.register(VARIABLE_MAPPING)
from .bird_meta_data_model import MAPPING_TO_CUBE
admin.site.register(MAPPING_TO_CUBE)
from .bird_meta_data_model import MAPPING_DEFINITION
admin.site.register(MAPPING_DEFINITION)
from .bird_meta_data_model import AXIS
admin.site.register(AXIS)
from .bird_meta_data_model import AXIS_ORDINATE
admin.site.register(AXIS_ORDINATE)
from .bird_meta_data_model import CELL_POSITION
admin.site.register(CELL_POSITION)
from .bird_meta_data_model import ORDINATE_ITEM
admin.site.register(ORDINATE_ITEM)
from .bird_meta_data_model import TABLE
admin.site.register(TABLE)
from .bird_meta_data_model import TABLE_CELL
admin.site.register(TABLE_CELL)
from .bird_meta_data_model import CUBE
admin.site.register(CUBE)
from .bird_meta_data_model import CUBE_STRUCTURE
admin.site.register(CUBE_STRUCTURE)
from .bird_meta_data_model import CUBE_STRUCTURE_ITEM
admin.site.register(CUBE_STRUCTURE_ITEM)
from .bird_meta_data_model import CUBE_LINK
admin.site.register(CUBE_LINK)
from .bird_meta_data_model import CUBE_STRUCTURE_ITEM_LINK
admin.site.register(CUBE_STRUCTURE_ITEM_LINK)
from .bird_meta_data_model import COMBINATION
admin.site.register(COMBINATION)
from .bird_meta_data_model import COMBINATION_ITEM
admin.site.register(COMBINATION_ITEM)
from .bird_meta_data_model import CUBE_TO_COMBINATION
admin.site.register(CUBE_TO_COMBINATION)
from .bird_meta_data_model import SUBDOMAIN_ENUMERATION
admin.site.register(SUBDOMAIN_ENUMERATION)
from .bird_meta_data_model import VARIABLE_SET
admin.site.register(VARIABLE_SET)
from .bird_meta_data_model import VARIABLE_SET_ENUMERATION
admin.site.register(VARIABLE_SET_ENUMERATION)
from .bird_meta_data_model import MEMBER_LINK
admin.site.register(MEMBER_LINK)


from .bird_data_model import ABSTRCT_INSTRMNT_RL
admin.site.register(ABSTRCT_INSTRMNT_RL)
from .bird_data_model import ACCNTNG_CNSLDTN_GRP
admin.site.register(ACCNTNG_CNSLDTN_GRP)
from .bird_data_model import ADVNC
admin.site.register(ADVNC)
from .bird_data_model import ADVNC_CRDTR_ASSGNMNT
admin.site.register(ADVNC_CRDTR_ASSGNMNT)
from .bird_data_model import ADVNC_DBTR_ASSGNMNT
admin.site.register(ADVNC_DBTR_ASSGNMNT)
from .bird_data_model import ARCRFT_CLLTRL
admin.site.register(ARCRFT_CLLTRL)
from .bird_data_model import ABS
admin.site.register(ABS)
from .bird_data_model import ASST_PL_CVRD_BND_PRGRM
admin.site.register(ASST_PL_CVRD_BND_PRGRM)
from .bird_data_model import ASST_PL_CRDT_TRNSFR
admin.site.register(ASST_PL_CRDT_TRNSFR)
from .bird_data_model import ASST_PL_SCRTSTN
admin.site.register(ASST_PL_SCRTSTN)
from .bird_data_model import ASST_PL
admin.site.register(ASST_PL)
from .bird_data_model import ASST_PL_EQT_INSTRMNT_NT_SCRT_ASSGNMNT
admin.site.register(ASST_PL_EQT_INSTRMNT_NT_SCRT_ASSGNMNT)
from .bird_data_model import ASST_PL_LN_ASSGNMNT
admin.site.register(ASST_PL_LN_ASSGNMNT)
from .bird_data_model import ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT
admin.site.register(ASST_PL_DBT_SCRTY_PSTN_ASSGNMNT)
from .bird_data_model import ASSNGND_DBTR
admin.site.register(ASSNGND_DBTR)
from .bird_data_model import ASSCT
admin.site.register(ASSCT)
from .bird_data_model import BLNC_SHT_NTTNG
admin.site.register(BLNC_SHT_NTTNG)
from .bird_data_model import BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN
admin.site.register(BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN)
from .bird_data_model import BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN_DRVD_DT
admin.site.register(BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN_DRVD_DT)
from .bird_data_model import BLNC_SHT_RCGNSD_ETD_LBLTY_PSTN
admin.site.register(BLNC_SHT_RCGNSD_ETD_LBLTY_PSTN)
from .bird_data_model import BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
admin.site.register(BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT)
from .bird_data_model import BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_IFRS
admin.site.register(BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_IFRS)
from .bird_data_model import BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_NGAAP
admin.site.register(BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_NGAAP)
from .bird_data_model import BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_DRVD_DT
admin.site.register(BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_DRVD_DT)
from .bird_data_model import BLNC_SHT_RCGNSD_FNNCNL_LBLTY_INSTRMNT
admin.site.register(BLNC_SHT_RCGNSD_FNNCNL_LBLTY_INSTRMNT)
from .bird_data_model import BNFCRY
admin.site.register(BNFCRY)
from .bird_data_model import BRRWR
admin.site.register(BRRWR)
from .bird_data_model import BRNCH
admin.site.register(BRNCH)
from .bird_data_model import BUYR
admin.site.register(BUYR)
from .bird_data_model import CSH_LG
admin.site.register(CSH_LG)
from .bird_data_model import CSH_HND
admin.site.register(CSH_HND)
from .bird_data_model import CNTRL_BNK
admin.site.register(CNTRL_BNK)
from .bird_data_model import CNTRL_BNK_CRPRTN
admin.site.register(CNTRL_BNK_CRPRTN)
from .bird_data_model import CNTRL_BNK_PRVT_SCTR_CMPNY
admin.site.register(CNTRL_BNK_PRVT_SCTR_CMPNY)
from .bird_data_model import CNTRL_BNK_PRVT_SCTR_CMPNY_RL
admin.site.register(CNTRL_BNK_PRVT_SCTR_CMPNY_RL)
from .bird_data_model import CB_NT_ECB
admin.site.register(CB_NT_ECB)
from .bird_data_model import CNTRL_CNTRPRTY_CLNT
admin.site.register(CNTRL_CNTRPRTY_CLNT)
from .bird_data_model import CNTRL_GVRNMNT
admin.site.register(CNTRL_GVRNMNT)
from .bird_data_model import CNTRL_GVRNMNT_RTNG_SYSTM
admin.site.register(CNTRL_GVRNMNT_RTNG_SYSTM)
from .bird_data_model import CLRNG_MMBR
admin.site.register(CLRNG_MMBR)
from .bird_data_model import CLLTRL
admin.site.register(CLLTRL)
from .bird_data_model import CLLTRL_ANNX
admin.site.register(CLLTRL_ANNX)
from .bird_data_model import CLLTRL_GVN_INSTRMNT
admin.site.register(CLLTRL_GVN_INSTRMNT)
from .bird_data_model import CLLTRL_NN_FNNCL_ASST_ASSGNMNT
admin.site.register(CLLTRL_NN_FNNCL_ASST_ASSGNMNT)
from .bird_data_model import CLLTRL_OBTND_TKNG_PSSSSN
admin.site.register(CLLTRL_OBTND_TKNG_PSSSSN)
from .bird_data_model import CLLTRL_OBTND_TKNG_PSSSSN_DRVD_DT
admin.site.register(CLLTRL_OBTND_TKNG_PSSSSN_DRVD_DT)
from .bird_data_model import CLLTRL_RCVD_INSTRMNT
admin.site.register(CLLTRL_RCVD_INSTRMNT)
from .bird_data_model import CLLTRL_RCVD_INSTRMNT_OBTND_TKNG_PSSSSN
admin.site.register(CLLTRL_RCVD_INSTRMNT_OBTND_TKNG_PSSSSN)
from .bird_data_model import CLLTRL_RCVD_INSTRMNT_OBTND_TKNG_PSSSSN_DRVD_DT
admin.site.register(CLLTRL_RCVD_INSTRMNT_OBTND_TKNG_PSSSSN_DRVD_DT)
from .bird_data_model import CMMRCL_RL_ESTT_OFFCS_CMMRCL_PRMSS_CLLTRL
admin.site.register(CMMRCL_RL_ESTT_OFFCS_CMMRCL_PRMSS_CLLTRL)
from .bird_data_model import CMMRCL_RL_ESTT_CLLTRL
admin.site.register(CMMRCL_RL_ESTT_CLLTRL)
from .bird_data_model import CMMDTY_CLLTRL
admin.site.register(CMMDTY_CLLTRL)
from .bird_data_model import CMMDTY_RSK_FCTR_FR_STNDRDSD_APPRCH
admin.site.register(CMMDTY_RSK_FCTR_FR_STNDRDSD_APPRCH)
from .bird_data_model import CVRD_BND
admin.site.register(CVRD_BND)
from .bird_data_model import CVRD_BND_ISSNC
admin.site.register(CVRD_BND_ISSNC)
from .bird_data_model import CVRD_BND_PRGRM
admin.site.register(CVRD_BND_PRGRM)
from .bird_data_model import CRDT_CRD_DBT
admin.site.register(CRDT_CRD_DBT)
from .bird_data_model import CRDT_CRD_DBT_CRDTR_ASSGNMNT
admin.site.register(CRDT_CRD_DBT_CRDTR_ASSGNMNT)
from .bird_data_model import CRDT_CRD_DBT_DBTR_ASSGNMNT
admin.site.register(CRDT_CRD_DBT_DBTR_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY
admin.site.register(CRDT_FCLTY)
from .bird_data_model import CRDT_FCLTY_CLLTRL_ASSGNMNT
admin.site.register(CRDT_FCLTY_CLLTRL_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT
admin.site.register(CRDT_FCLTY_CLLTRL_RCVD_INSTRMNT_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_CRDTR_ASSGNMNT
admin.site.register(CRDT_FCLTY_CRDTR_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_DBTR_ASSGNMNT
admin.site.register(CRDT_FCLTY_DBTR_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_ENTTY_RL_ASSGNMNT
admin.site.register(CRDT_FCLTY_ENTTY_RL_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_RSK_DT
admin.site.register(CRDT_FCLTY_RSK_DT)
from .bird_data_model import CRDT_FCLTY_RSK_DT_DRVD_DT
admin.site.register(CRDT_FCLTY_RSK_DT_DRVD_DT)
from .bird_data_model import CRDT_FCLTY_SRVCR_ASSGNMNT
admin.site.register(CRDT_FCLTY_SRVCR_ASSGNMNT)
from .bird_data_model import CRDT_FCLTY_INTRST_RT
admin.site.register(CRDT_FCLTY_INTRST_RT)
from .bird_data_model import CRDT_INSTTTN
admin.site.register(CRDT_INSTTTN)
from .bird_data_model import CRDTR
admin.site.register(CRDTR)
from .bird_data_model import CRDT_RSK_MTGTN_ARRGMNT
admin.site.register(CRDT_RSK_MTGTN_ARRGMNT)
from .bird_data_model import CRDT_RSK_MTGTN_ASSGNMNT
admin.site.register(CRDT_RSK_MTGTN_ASSGNMNT)
from .bird_data_model import CRDT_SPRD_RSK_NN_SCRTSTN_RSK_FCTR_STNDRDSD_APPRCH
admin.site.register(CRDT_SPRD_RSK_NN_SCRTSTN_RSK_FCTR_STNDRDSD_APPRCH)
from .bird_data_model import CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM
admin.site.register(CRDT_TRNSFR_OTHR_SCRTSTN_CVRD_BND_PRGRM)
from .bird_data_model import CRRNCY_CLLTRL
admin.site.register(CRRNCY_CLLTRL)
from .bird_data_model import CRRNT_TX_ASST
admin.site.register(CRRNT_TX_ASST)
from .bird_data_model import CRRNT_TX_LBLTY
admin.site.register(CRRNT_TX_LBLTY)
from .bird_data_model import CRVTR
admin.site.register(CRVTR)
from .bird_data_model import DBT_SCRTY
admin.site.register(DBT_SCRTY)
from .bird_data_model import DBT_SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT
admin.site.register(DBT_SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT)
from .bird_data_model import DBT_SCRTY_DBTR_ASSGNMNT
admin.site.register(DBT_SCRTY_DBTR_ASSGNMNT)
from .bird_data_model import DBT_SCRTY_DRVD_DT
admin.site.register(DBT_SCRTY_DRVD_DT)
from .bird_data_model import DBT_SCRTY_IFRS
admin.site.register(DBT_SCRTY_IFRS)
from .bird_data_model import DBT_SCRTY_NGAAP
admin.site.register(DBT_SCRTY_NGAAP)
from .bird_data_model import DBT_SCRTY_ISSD
admin.site.register(DBT_SCRTY_ISSD)
from .bird_data_model import DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT
admin.site.register(DBT_SCRTY_ISSD_TRDTNL_SCRTSTN_ASSGNMNT)
from .bird_data_model import DBT_SCRTY_PSTN_HDGD_OTC_DRVTV
admin.site.register(DBT_SCRTY_PSTN_HDGD_OTC_DRVTV)
from .bird_data_model import DBT_SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT
admin.site.register(DBT_SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT)
from .bird_data_model import DBT_SCRTY_STHT_UNDRLYNG_ASSTS
admin.site.register(DBT_SCRTY_STHT_UNDRLYNG_ASSTS)
from .bird_data_model import DBT_SCRTY_WTH_UNDRLYNG_ASSTS
admin.site.register(DBT_SCRTY_WTH_UNDRLYNG_ASSTS)
from .bird_data_model import DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD
admin.site.register(DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD)
from .bird_data_model import DFRRD_TX_ASST
admin.site.register(DFRRD_TX_ASST)
from .bird_data_model import DFRRD_TX_LBLTY
admin.site.register(DFRRD_TX_LBLTY)
from .bird_data_model import DLT_SNSTVTY
admin.site.register(DLT_SNSTVTY)
from .bird_data_model import DPST
admin.site.register(DPST)
from .bird_data_model import DPST_DPSTR_ASSGNMNT
admin.site.register(DPST_DPSTR_ASSGNMNT)
from .bird_data_model import DPST_DPST_TKNG_CRPRTN_ASSGNMNT
admin.site.register(DPST_DPST_TKNG_CRPRTN_ASSGNMNT)
from .bird_data_model import DPSTR
admin.site.register(DPSTR)
from .bird_data_model import DPST_RDMBL_NTC
admin.site.register(DPST_RDMBL_NTC)
from .bird_data_model import DPST_TKNG_CRPRTN
admin.site.register(DPST_TKNG_CRPRTN)
from .bird_data_model import DPST_WTH_AGRD_MTRTY
admin.site.register(DPST_WTH_AGRD_MTRTY)
from .bird_data_model import DSCRNT_EXCSS_SPRD
admin.site.register(DSCRNT_EXCSS_SPRD)
from .bird_data_model import DMSTC_BRNCH
admin.site.register(DMSTC_BRNCH)
from .bird_data_model import DMSTC_INSTTTNL_UNT
admin.site.register(DMSTC_INSTTTNL_UNT)
from .bird_data_model import EMPLY_BNFT
admin.site.register(EMPLY_BNFT)
from .bird_data_model import ENTTY_GRP_RL
admin.site.register(ENTTY_GRP_RL)
from .bird_data_model import ENTTY_RL
admin.site.register(ENTTY_RL)
from .bird_data_model import ENTTY_TRNSCTN_RL
admin.site.register(ENTTY_TRNSCTN_RL)
from .bird_data_model import EQTY_FND_SCRTY
admin.site.register(EQTY_FND_SCRTY)
from .bird_data_model import EQT_INSTRMNT_LG
admin.site.register(EQT_INSTRMNT_LG)
from .bird_data_model import EQT_INSTRMNT_LG_EQT_INSTRMNT_NT_SCRT_ASSGNMNT
admin.site.register(EQT_INSTRMNT_LG_EQT_INSTRMNT_NT_SCRT_ASSGNMNT)
from .bird_data_model import EQT_INSTRMNT_NT_SCRT
admin.site.register(EQT_INSTRMNT_NT_SCRT)
from .bird_data_model import EQTY_INSTRMNT_NT_SCRTY_INVSTR_ASSGNMNT
admin.site.register(EQTY_INSTRMNT_NT_SCRTY_INVSTR_ASSGNMNT)
from .bird_data_model import EQTY_INSTRMNT_NT_SCRTY_ISSR_ASSGNMNT
admin.site.register(EQTY_INSTRMNT_NT_SCRTY_ISSR_ASSGNMNT)
from .bird_data_model import EQTY_FND_SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT
admin.site.register(EQTY_FND_SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT)
from .bird_data_model import EQTY_FND_SCRTY_PSTN_HDGD_OTC_DRVTV
admin.site.register(EQTY_FND_SCRTY_PSTN_HDGD_OTC_DRVTV)
from .bird_data_model import EQTY_FND_SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT
admin.site.register(EQTY_FND_SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT)
from .bird_data_model import EQTY_RSK_FCTR
admin.site.register(EQTY_RSK_FCTR)
from .bird_data_model import EQTY_SCRTY
admin.site.register(EQTY_SCRTY)
from .bird_data_model import ECB
admin.site.register(ECB)
from .bird_data_model import EU_MMBR_PRTY
admin.site.register(EU_MMBR_PRTY)
from .bird_data_model import EXCHNG_TRDBL_DRVTV
admin.site.register(EXCHNG_TRDBL_DRVTV)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_ASST_LBLTY_PSTN
admin.site.register(EXCHNG_TRDBL_DRVTV_ASST_LBLTY_PSTN)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_ASST_PSTN
admin.site.register(EXCHNG_TRDBL_DRVTV_ASST_PSTN)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_CLLTRL
admin.site.register(EXCHNG_TRDBL_DRVTV_CLLTRL)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_LBLTY_PSTN
admin.site.register(EXCHNG_TRDBL_DRVTV_LBLTY_PSTN)
from .bird_data_model import ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT
admin.site.register(ETD_LBLTY_PSTN_SNTHTC_SCRTSTN_ASSGNMNT)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_PSTN
admin.site.register(EXCHNG_TRDBL_DRVTV_PSTN)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_HDG_PSTN
admin.site.register(EXCHNG_TRDBL_DRVTV_HDG_PSTN)
from .bird_data_model import EXCHNG_TRDBL_DRVTV_POSTN_RL
admin.site.register(EXCHNG_TRDBL_DRVTV_POSTN_RL)
from .bird_data_model import EXCHNG_TRDBL_FTR
admin.site.register(EXCHNG_TRDBL_FTR)
from .bird_data_model import EXCHNG_TRDBL_OPTN
admin.site.register(EXCHNG_TRDBL_OPTN)
from .bird_data_model import FCTR
admin.site.register(FCTR)
from .bird_data_model import FCTRNG
admin.site.register(FCTRNG)
from .bird_data_model import FCTRNG_CSH_RSRV
admin.site.register(FCTRNG_CSH_RSRV)
from .bird_data_model import FR_VLD_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN
admin.site.register(FR_VLD_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN)
from .bird_data_model import FV_EXCHNG_TRDBL_DRVTV_LBLTY_PSTN
admin.site.register(FV_EXCHNG_TRDBL_DRVTV_LBLTY_PSTN)
from .bird_data_model import FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
admin.site.register(FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT)
from .bird_data_model import FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT
admin.site.register(FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT)
from .bird_data_model import FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT_IFRS
admin.site.register(FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT_IFRS)
from .bird_data_model import FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT_NGAAP
admin.site.register(FR_VLD_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT_NGAAP)
from .bird_data_model import FV_DBT_SCRTY_ISSD
admin.site.register(FV_DBT_SCRTY_ISSD)
from .bird_data_model import FNNCL_ASST_INSTRMNT
admin.site.register(FNNCL_ASST_INSTRMNT)
from .bird_data_model import FNNCL_ASST_INSTRMNT_DBTR_ASSSSD
admin.site.register(FNNCL_ASST_INSTRMNT_DBTR_ASSSSD)
from .bird_data_model import FNNCL_ASST_INSTRMNT_DRVD_DT
admin.site.register(FNNCL_ASST_INSTRMNT_DRVD_DT)
from .bird_data_model import FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD
admin.site.register(FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD)
from .bird_data_model import FNNCL_CLLTRL
admin.site.register(FNNCL_CLLTRL)
from .bird_data_model import FNNCL_CNTRCT
admin.site.register(FNNCL_CNTRCT)
from .bird_data_model import FNNCL_CRPRTN
admin.site.register(FNNCL_CRPRTN)
from .bird_data_model import FNNCL_GRNT_INSTRMNT
admin.site.register(FNNCL_GRNT_INSTRMNT)
from .bird_data_model import FNNCL_GRNT_INSTRMNT_BNFCRY_ASSGNMNT
admin.site.register(FNNCL_GRNT_INSTRMNT_BNFCRY_ASSGNMNT)
from .bird_data_model import FNNCL_GRNT_INSTRMNT_DBT_SCRT
admin.site.register(FNNCL_GRNT_INSTRMNT_DBT_SCRT)
from .bird_data_model import FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT
admin.site.register(FNNCL_GRNT_INSTRMNT_DBT_SCRT_DBT_SCRTY_ASSGNMNT)
from .bird_data_model import FNNCL_GRNT_INSTMNT_NT_DBT_SCTY
admin.site.register(FNNCL_GRNT_INSTMNT_NT_DBT_SCTY)
from .bird_data_model import FNNCL_GRNT_INSTRMNT_PRTCTN_PRVDR_ASSGNMNT
admin.site.register(FNNCL_GRNT_INSTRMNT_PRTCTN_PRVDR_ASSGNMNT)
from .bird_data_model import FNNCL_LS
admin.site.register(FNNCL_LS)
from .bird_data_model import FNNCL_LS_LSS_ASSGNMNT
admin.site.register(FNNCL_LS_LSS_ASSGNMNT)
from .bird_data_model import FNNCL_LS_LSSR_ASSGNMNT
admin.site.register(FNNCL_LS_LSSR_ASSGNMNT)
from .bird_data_model import FNNCL_LBLTY_INSTRMNT
admin.site.register(FNNCL_LBLTY_INSTRMNT)
from .bird_data_model import FXD_INTRST_FNNCL_ASST_INSTRMNT
admin.site.register(FXD_INTRST_FNNCL_ASST_INSTRMNT)
from .bird_data_model import FRBRN_LNG_NN_NGTBL_SCRTY_PSTN
admin.site.register(FRBRN_LNG_NN_NGTBL_SCRTY_PSTN)
from .bird_data_model import FRBN_OFF_BLNC_SHT_ITM_GVN_INSTRMNT
admin.site.register(FRBN_OFF_BLNC_SHT_ITM_GVN_INSTRMNT)
from .bird_data_model import FRGN_BRNCH
admin.site.register(FRGN_BRNCH)
from .bird_data_model import FX_RSK_FACTR_SA
admin.site.register(FX_RSK_FACTR_SA)
from .bird_data_model import FRGN_INSTTTNL_UNT
admin.site.register(FRGN_INSTTTNL_UNT)
from .bird_data_model import FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR
admin.site.register(FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR)
from .bird_data_model import FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS
admin.site.register(FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_ETD_PSTNS)
from .bird_data_model import FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS
admin.site.register(FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_OTC_PSTNS)
from .bird_data_model import FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS
admin.site.register(FNDMNTL_RVW_TRDNG_BK_STNDRD_APPRCH_RSK_MSR_FR_SCRTY_PSTNS)
from .bird_data_model import FND_SCRTY
admin.site.register(FND_SCRTY)
from .bird_data_model import FNDS_GNRL_BNKNG_RSK
admin.site.register(FNDS_GNRL_BNKNG_RSK)
from .bird_data_model import GNRL_GVRNMNT
admin.site.register(GNRL_GVRNMNT)
from .bird_data_model import GIRR_RSK_FCTR
admin.site.register(GIRR_RSK_FCTR)
from .bird_data_model import GLD_CLLTRL
admin.site.register(GLD_CLLTRL)
from .bird_data_model import GDWLL
admin.site.register(GDWLL)
from .bird_data_model import GRDD_RTNG_SYSTM
admin.site.register(GRDD_RTNG_SYSTM)
from .bird_data_model import GRP
admin.site.register(GRP)
from .bird_data_model import GRP_CLNTS
admin.site.register(GRP_CLNTS)
from .bird_data_model import GRP_CLNTS_KY_MNGMNT_PRSNLL_ASSGNMNT
admin.site.register(GRP_CLNTS_KY_MNGMNT_PRSNLL_ASSGNMNT)
from .bird_data_model import GRP_CNNCTD_CLNTS
admin.site.register(GRP_CNNCTD_CLNTS)
from .bird_data_model import GRP_CNSLDTD_CLNTS
admin.site.register(GRP_CNSLDTD_CLNTS)
from .bird_data_model import IMMTRL_RGHTS_CLLTRL
admin.site.register(IMMTRL_RGHTS_CLLTRL)
from .bird_data_model import IMMTRL_RGHTS_CLLTRL_OTHR_INTNGBL_ASST_NT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(IMMTRL_RGHTS_CLLTRL_OTHR_INTNGBL_ASST_NT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import IMMTRL_RGHTS_CLLTRL_OTHR_INTNGBL_ASST_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(IMMTRL_RGHTS_CLLTRL_OTHR_INTNGBL_ASST_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import IMMDT_PRTNR_ENTRPRS
admin.site.register(IMMDT_PRTNR_ENTRPRS)
from .bird_data_model import IMMDT_PRNT_ENTRPRS_ASSGNMNT
admin.site.register(IMMDT_PRNT_ENTRPRS_ASSGNMNT)
from .bird_data_model import INSTTTNL_UNT_FRGN_BRNCHS
admin.site.register(INSTTTNL_UNT_FRGN_BRNCHS)
from .bird_data_model import INSTRMNT
admin.site.register(INSTRMNT)
from .bird_data_model import INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT
admin.site.register(INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT)
from .bird_data_model import INSTRMNT_ENTTY_RL_ASSGNMNT
admin.site.register(INSTRMNT_ENTTY_RL_ASSGNMNT)
from .bird_data_model import INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV
admin.site.register(INSTRMNT_HDGD_EXCHNG_TRDBL_DRVTV)
from .bird_data_model import INSTRMNT_HDGD_OTC_DRVTV
admin.site.register(INSTRMNT_HDGD_OTC_DRVTV)
from .bird_data_model import INSTRMNT_PRTCN_ARRNGMNT_ASSGNMNT
admin.site.register(INSTRMNT_PRTCN_ARRNGMNT_ASSGNMNT)
from .bird_data_model import INSTRMNT_RSLTNG_DRCTLY_FNNCL_CNTRCT
admin.site.register(INSTRMNT_RSLTNG_DRCTLY_FNNCL_CNTRCT)
from .bird_data_model import INSTRMNT_RSLTNG_CRDT_FCLTY
admin.site.register(INSTRMNT_RSLTNG_CRDT_FCLTY)
from .bird_data_model import INSTRMNT_RL
admin.site.register(INSTRMNT_RL)
from .bird_data_model import INSTRMNT_SRVCR_ASSGNMNT
admin.site.register(INSTRMNT_SRVCR_ASSGNMNT)
from .bird_data_model import INTRST_ONL_FNNCL_ASST_INSTRMNT
admin.site.register(INTRST_ONL_FNNCL_ASST_INSTRMNT)
from .bird_data_model import INTRST_RT_RSK_HDG_PRTFL
admin.site.register(INTRST_RT_RSK_HDG_PRTFL)
from .bird_data_model import INTRNL_CNSLDTN_GRP
admin.site.register(INTRNL_CNSLDTN_GRP)
from .bird_data_model import INTRNL_GRP
admin.site.register(INTRNL_GRP)
from .bird_data_model import INTRNL_GRP_KY_MNGMNT_PRSNLL_ASSGNMNT
admin.site.register(INTRNL_GRP_KY_MNGMNT_PRSNLL_ASSGNMNT)
from .bird_data_model import INTRNL_GRP_RL
admin.site.register(INTRNL_GRP_RL)
from .bird_data_model import INTRNTNL_ORGNSTN
admin.site.register(INTRNTNL_ORGNSTN)
from .bird_data_model import INTRNTNL_ORGNSTN_GNRL_GVNMNT
admin.site.register(INTRNTNL_ORGNSTN_GNRL_GVNMNT)
from .bird_data_model import ISIN_SCRTY
admin.site.register(ISIN_SCRTY)
from .bird_data_model import INVNTRY_CLLTRL
admin.site.register(INVNTRY_CLLTRL)
from .bird_data_model import INVSTMNT_PRPRTY
admin.site.register(INVSTMNT_PRPRTY)
from .bird_data_model import INVSTMNT_VHCL_FND
admin.site.register(INVSTMNT_VHCL_FND)
from .bird_data_model import INVSTR
admin.site.register(INVSTR)
from .bird_data_model import ISS_BSD_RTNG_SYSTM
admin.site.register(ISS_BSD_RTNG_SYSTM)
from .bird_data_model import DBT_SCRTY_ISSD_BNKNG_BK
admin.site.register(DBT_SCRTY_ISSD_BNKNG_BK)
from .bird_data_model import DBT_SCRTY_ISSD_TRDNG_BK
admin.site.register(DBT_SCRTY_ISSD_TRDNG_BK)
from .bird_data_model import DBT_SCRTY_ISSD_TRDNG_BK_IFRS
admin.site.register(DBT_SCRTY_ISSD_TRDNG_BK_IFRS)
from .bird_data_model import DBT_SCRTY_ISSD_TRDNG_BK_NGAAP
admin.site.register(DBT_SCRTY_ISSD_TRDNG_BK_NGAAP)
from .bird_data_model import ISSR
admin.site.register(ISSR)
from .bird_data_model import ISSR_BSD_RTNG_SYSTM
admin.site.register(ISSR_BSD_RTNG_SYSTM)
from .bird_data_model import JNT_VNTR
admin.site.register(JNT_VNTR)
from .bird_data_model import KY_MNGMNT_PRSNLL
admin.site.register(KY_MNGMNT_PRSNLL)
from .bird_data_model import LND_EXCLDNG_AGRCLTR
admin.site.register(LND_EXCLDNG_AGRCLTR)
from .bird_data_model import LND_INCLDNG_AGRCLTR
admin.site.register(LND_INCLDNG_AGRCLTR)
from .bird_data_model import LGL_ENTTY_ID_PRTY_CD
admin.site.register(LGL_ENTTY_ID_PRTY_CD)
from .bird_data_model import LGL_PRSN
admin.site.register(LGL_PRSN)
from .bird_data_model import LGL_PRSN_RL
admin.site.register(LGL_PRSN_RL)
from .bird_data_model import LNDR
admin.site.register(LNDR)
from .bird_data_model import LS
admin.site.register(LS)
from .bird_data_model import LSSR
admin.site.register(LSSR)
from .bird_data_model import LF_INSRNC_PLCY_PLDGD
admin.site.register(LF_INSRNC_PLCY_PLDGD)
from .bird_data_model import LNKD_ENTRPRS
admin.site.register(LNKD_ENTRPRS)
from .bird_data_model import LNKD_ENTRPRS_ASSGNMNT
admin.site.register(LNKD_ENTRPRS_ASSGNMNT)
from .bird_data_model import LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY
admin.site.register(LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNCE
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT_AND_ADVNCE)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT_CLLTRL_ASSGNMNT
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT_CLLTRL_ASSGNMNT)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT_CLLTRL_ASSGNMNT_DRVD_DT
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT_CLLTRL_ASSGNMNT_DRVD_DT)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT_ADVNC_DRVD_DT
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT_ADVNC_DRVD_DT)
from .bird_data_model import LN_EXCLDNG_RPRCHS_AGRMNT_DRVD_DT
admin.site.register(LN_EXCLDNG_RPRCHS_AGRMNT_DRVD_DT)
from .bird_data_model import LN_AND_ADVNC_LG_LN_AND_ADVNC_ASSGNMNT
admin.site.register(LN_AND_ADVNC_LG_LN_AND_ADVNC_ASSGNMNT)
from .bird_data_model import LN_DBTR
admin.site.register(LN_DBTR)
from .bird_data_model import LN_AND_ADVNC_LG
admin.site.register(LN_AND_ADVNC_LG)
from .bird_data_model import LNG_SBT_SCRTY_PSTN
admin.site.register(LNG_SBT_SCRTY_PSTN)
from .bird_data_model import LNG_SBT_SCRTY_PSTN_DRVD_DT
admin.site.register(LNG_SBT_SCRTY_PSTN_DRVD_DT)
from .bird_data_model import LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
admin.site.register(LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT)
from .bird_data_model import LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
admin.site.register(LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT)
from .bird_data_model import LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASST_ASSGNMNT_IFRS
admin.site.register(LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASST_ASSGNMNT_IFRS)
from .bird_data_model import LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASST_ASSGNMNT_NGAAP
admin.site.register(LNG_DBT_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASST_ASSGNMNT_NGAAP)
from .bird_data_model import LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ENCMBRNC_DT
admin.site.register(LNG_DBT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ENCMBRNC_DT)
from .bird_data_model import LNG_EQTY_FND_SCRYT_PSTN
admin.site.register(LNG_EQTY_FND_SCRYT_PSTN)
from .bird_data_model import LND_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
admin.site.register(LND_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT)
from .bird_data_model import LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS
admin.site.register(LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_IFRS)
from .bird_data_model import LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_NGAAP
admin.site.register(LNG_EQUTY_FND_SCRTY_PSTN_PRDNTL_PRFL_ASSGNMNT_ACCNTNG_CLSSFCTN_ASST_ASSGNMNT_NGAAP)
from .bird_data_model import LNG_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
admin.site.register(LNG_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT)
from .bird_data_model import LNG_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ENCMBRNC_DT
admin.site.register(LNG_EQTY_FND_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ENCMBRNC_DT)
from .bird_data_model import LNG_NGTBL_SCRTY_PSTN
admin.site.register(LNG_NGTBL_SCRTY_PSTN)
from .bird_data_model import LNG_NN_NGTBL_SCRTY_PSTN
admin.site.register(LNG_NN_NGTBL_SCRTY_PSTN)
from .bird_data_model import LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT
admin.site.register(LNG_NN_NGTBL_SCRTY_PSTN_CLLTRL_ASSGNMNT)
from .bird_data_model import LNG_NN_NGTBL_SCRTY_PSTNDRVD_DT
admin.site.register(LNG_NN_NGTBL_SCRTY_PSTNDRVD_DT)
from .bird_data_model import LNG_SCRTY_PSTN
admin.site.register(LNG_SCRTY_PSTN)
from .bird_data_model import LNG_SCRTY_PSTN_BNKG_BK_ASSGNMNT
admin.site.register(LNG_SCRTY_PSTN_BNKG_BK_ASSGNMNT)
from .bird_data_model import LNG_SCRTY_PSTN_DRVD_DT
admin.site.register(LNG_SCRTY_PSTN_DRVD_DT)
from .bird_data_model import DBT_SCRTY_PRTCTN_ARRNGMNT_ASSGNMNT
admin.site.register(DBT_SCRTY_PRTCTN_ARRNGMNT_ASSGNMNT)
from .bird_data_model import LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_ASSGNMNT_DRVD_DT
admin.site.register(LNG_SCRTY_PSTN_PRTCTN_ARRNGMNT_ASSGNMNT_DRVD_DT)
from .bird_data_model import LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
admin.site.register(LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT)
from .bird_data_model import LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
admin.site.register(LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT)
from .bird_data_model import LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT
admin.site.register(LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FR_FNNCL_ASSTS_ASSGNMNT_DRVD_DT)
from .bird_data_model import LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT
admin.site.register(LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_RSK_DT)
from .bird_data_model import LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT
admin.site.register(LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT)
from .bird_data_model import LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT_IFRS
admin.site.register(LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT_IFRS)
from .bird_data_model import LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT_NGAAP
admin.site.register(LNG_SCRTY_PSTN_TRDNG_BK_ASSGNMNT_NGAAP)
from .bird_data_model import MCHNRY_EQUPMNT_CLLTRL
admin.site.register(MCHNRY_EQUPMNT_CLLTRL)
from .bird_data_model import MSTR_AGRMNT
admin.site.register(MSTR_AGRMNT)
from .bird_data_model import MSTR_AGRMNT_CCP_ASSGNMNT
admin.site.register(MSTR_AGRMNT_CCP_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_CLRNG_MMBR_ASSGNMNT
admin.site.register(MSTR_AGRMNT_CLRNG_MMBR_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_ENTTY_RL_ASSGNMNT
admin.site.register(MSTR_AGRMNT_ENTTY_RL_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT
admin.site.register(MSTR_AGRMNT_FNNCL_CNTRCT_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_NN_QCCP_ASSGNMNT
admin.site.register(MSTR_AGRMNT_NN_QCCP_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_QCCP_ASSGNMNT
admin.site.register(MSTR_AGRMNT_QCCP_ASSGNMNT)
from .bird_data_model import MSTR_AGRMNT_WIT_CCP
admin.site.register(MSTR_AGRMNT_WIT_CCP)
from .bird_data_model import MSTR_AGRMNT_WIT_CLRNG_MMBR
admin.site.register(MSTR_AGRMNT_WIT_CLRNG_MMBR)
from .bird_data_model import MSTR_AGRMNT_WIT_NN_QCCP
admin.site.register(MSTR_AGRMNT_WIT_NN_QCCP)
from .bird_data_model import MSTR_AGRMNT_WIT_QCCP
admin.site.register(MSTR_AGRMNT_WIT_QCCP)
from .bird_data_model import MSTR_NTTNG_CNTRPRTY
admin.site.register(MSTR_NTTNG_CNTRPRTY)
from .bird_data_model import NTRL_PRSN
admin.site.register(NTRL_PRSN)
from .bird_data_model import NTRL_PRSN_GRP_RL
admin.site.register(NTRL_PRSN_GRP_RL)
from .bird_data_model import NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT
admin.site.register(NTRL_PRSN_KY_MNGMNT_PRSNLL_ASSGNMNT)
from .bird_data_model import NN_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN
admin.site.register(NN_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN)
from .bird_data_model import NN_BLNC_SHT_RCGNSD_ETD_LBLTY_PSTN
admin.site.register(NN_BLNC_SHT_RCGNSD_ETD_LBLTY_PSTN)
from .bird_data_model import NN_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
admin.site.register(NN_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT
admin.site.register(NN_BLNC_SHT_RCGNSD_FNNCL_LBLTY_INSTRMNT)
from .bird_data_model import NN_CNTRL_GVRNMNT_RTNG_SYSTM
admin.site.register(NN_CNTRL_GVRNMNT_RTNG_SYSTM)
from .bird_data_model import NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD
admin.site.register(NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD)
from .bird_data_model import NT_MMBR_EU
admin.site.register(NT_MMBR_EU)
from .bird_data_model import NN_FR_VLD_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN
admin.site.register(NN_FR_VLD_BLNC_SHT_RCGNSD_EXCHNG_TRDBL_DRVTV_ASST_PSTN)
from .bird_data_model import NFV_ETD_LBLTY_PSTN
admin.site.register(NFV_ETD_LBLTY_PSTN)
from .bird_data_model import NN_FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
admin.site.register(NN_FR_VLD_BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_FR_VLD_BLNC_SHT_ITM_GVN_CRDT_FCLTY
admin.site.register(NN_FR_VLD_BLNC_SHT_ITM_GVN_CRDT_FCLTY)
from .bird_data_model import NN_FV_DBT_SCRTY_ISSD
admin.site.register(NN_FV_DBT_SCRTY_ISSD)
from .bird_data_model import NN_FNNCL_ASST
admin.site.register(NN_FNNCL_ASST)
from .bird_data_model import NN_FNNCL_ASST_NN_FNNCL_LBLTY
admin.site.register(NN_FNNCL_ASST_NN_FNNCL_LBLTY)
from .bird_data_model import NN_FNNCL_CRPRTN
admin.site.register(NN_FNNCL_CRPRTN)
from .bird_data_model import NN_FNNCL_LBLTY
admin.site.register(NN_FNNCL_LBLTY)
from .bird_data_model import NN_FXD_INTRST_FNNCL_ASST_INSTRMNT
admin.site.register(NN_FXD_INTRST_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_FRBRN_LNG_NN_NGTBL_SCRTY_PSTN
admin.site.register(NN_FRBRN_LNG_NN_NGTBL_SCRTY_PSTN)
from .bird_data_model import NN_FRBN_OFF_BLNC_SHT_ITM_GVN_INSTRMNT
admin.site.register(NN_FRBN_OFF_BLNC_SHT_ITM_GVN_INSTRMNT)
from .bird_data_model import NN_INTRST_ONL_FNNCL_ASST_INSTRMNT
admin.site.register(NN_INTRST_ONL_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_ISIN_SCRTY_DRVD_DT
admin.site.register(NN_ISIN_SCRTY_DRVD_DT)
from .bird_data_model import NN_ISIN_SCRTY
admin.site.register(NN_ISIN_SCRTY)
from .bird_data_model import NN_LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY
admin.site.register(NN_LSTD_CNTRL_BNK_PRVT_SCTR_CMPNY)
from .bird_data_model import NN_PRFRMNG_DBT_SCRTY
admin.site.register(NN_PRFRMNG_DBT_SCRTY)
from .bird_data_model import NN_PRFRMNG_FNNCL_ASST_INSTRMNT_DBTR_ASSSSD
admin.site.register(NN_PRFRMNG_FNNCL_ASST_INSTRMNT_DBTR_ASSSSD)
from .bird_data_model import NN_PRFRMNG_NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD
admin.site.register(NN_PRFRMNG_NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD)
from .bird_data_model import NN_PRFRMNG_NN_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT
admin.site.register(NN_PRFRMNG_NN_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_PRPTL_DBT_SCRTY
admin.site.register(NN_PRPTL_DBT_SCRTY)
from .bird_data_model import NN_QCCP
admin.site.register(NN_QCCP)
from .bird_data_model import NN_RGSTRD_CLLTRL
admin.site.register(NN_RGSTRD_CLLTRL)
from .bird_data_model import NN_RNGTTD_FNNCL_ASST_INSTRMNT
admin.site.register(NN_RNGTTD_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_RTL_EXPSR_FNNCL_ASST_INSTRMNT
admin.site.register(NN_RTL_EXPSR_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NN_SLF_EMPLYD_NTRL_PRSN
admin.site.register(NN_SLF_EMPLYD_NTRL_PRSN)
from .bird_data_model import NN_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN
admin.site.register(NN_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN)
from .bird_data_model import NN_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN
admin.site.register(NN_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN)
from .bird_data_model import NN_UPU_SYSTM_PRTY
admin.site.register(NN_UPU_SYSTM_PRTY)
from .bird_data_model import CLLTRL_NT_OBTND
admin.site.register(CLLTRL_NT_OBTND)
from .bird_data_model import CLLTRL_OBTND
admin.site.register(CLLTRL_OBTND)
from .bird_data_model import NT_PST_DU_FNNCL_ASST_INSTRMNT
admin.site.register(NT_PST_DU_FNNCL_ASST_INSTRMNT)
from .bird_data_model import NT_SGNFCNT_RSK_TRNSFR_SCRTSTN
admin.site.register(NT_SGNFCNT_RSK_TRNSFR_SCRTSTN)
from .bird_data_model import NMRC_RTNG_SYSTM
admin.site.register(NMRC_RTNG_SYSTM)
from .bird_data_model import OFF_BLNC_INSTRMNT
admin.site.register(OFF_BLNC_INSTRMNT)
from .bird_data_model import OFF_BLNC_INSTRMNT_CLLTRL_ASSGNMNT
admin.site.register(OFF_BLNC_INSTRMNT_CLLTRL_ASSGNMNT)
from .bird_data_model import OFF_BLNC_SHT_ITM_GVN_INSTRMNT
admin.site.register(OFF_BLNC_SHT_ITM_GVN_INSTRMNT)
from .bird_data_model import OFF_BLNC_SHT_ITM_GVN_INSTRMNT_DRVD_DT
admin.site.register(OFF_BLNC_SHT_ITM_GVN_INSTRMNT_DRVD_DT)
from .bird_data_model import OFF_BLNC_SHT_ITM_RCVD_INSTRMNT
admin.site.register(OFF_BLNC_SHT_ITM_RCVD_INSTRMNT)
from .bird_data_model import OFFCS_CMMRCL_PRMSS_CLLTRL
admin.site.register(OFFCS_CMMRCL_PRMSS_CLLTRL)
from .bird_data_model import OFFCS_CMMRCL_PRMSS_NT_RLTD_LND_CLLTRL
admin.site.register(OFFCS_CMMRCL_PRMSS_NT_RLTD_LND_CLLTRL)
from .bird_data_model import OFFCS_CMMRCL_PRMSS_RLTD_LND_CLLTRL
admin.site.register(OFFCS_CMMRCL_PRMSS_RLTD_LND_CLLTRL)
from .bird_data_model import OPN_RPRCHS_AGRMNT_INSTRMNT
admin.site.register(OPN_RPRCHS_AGRMNT_INSTRMNT)
from .bird_data_model import ORGNSTN
admin.site.register(ORGNSTN)
from .bird_data_model import ORGNSTNL_UNT
admin.site.register(ORGNSTNL_UNT)
from .bird_data_model import ORGNSTN_RSK_DT
admin.site.register(ORGNSTN_RSK_DT)
from .bird_data_model import ORGNSTN_RL
admin.site.register(ORGNSTN_RL)
from .bird_data_model import ORGNSTN_WTH_LGL_PRCDNG
admin.site.register(ORGNSTN_WTH_LGL_PRCDNG)
from .bird_data_model import ORGNSTN_WTHT_LGL_PRCDNG
admin.site.register(ORGNSTN_WTHT_LGL_PRCDNG)
from .bird_data_model import ORGNL_LNDR
admin.site.register(ORGNL_LNDR)
from .bird_data_model import ORGNTR
admin.site.register(ORGNTR)
from .bird_data_model import OTHR_ADVNC
admin.site.register(OTHR_ADVNC)
from .bird_data_model import OTHR_CLLTRL_RCVD_INSTRMNT
admin.site.register(OTHR_CLLTRL_RCVD_INSTRMNT)
from .bird_data_model import OTHR_CMMTMNT
admin.site.register(OTHR_CMMTMNT)
from .bird_data_model import OTHR_CMMTMNT_CRDTR_ASSGNMNT
admin.site.register(OTHR_CMMTMNT_CRDTR_ASSGNMNT)
from .bird_data_model import OTHR_CMMTMNT_DBTR_ASSGNMNT
admin.site.register(OTHR_CMMTMNT_DBTR_ASSGNMNT)
from .bird_data_model import OTHR_CMMDTY_CLLTRL
admin.site.register(OTHR_CMMDTY_CLLTRL)
from .bird_data_model import OTHR_DPST
admin.site.register(OTHR_DPST)
from .bird_data_model import OTHR_EMPLY_BNFT
admin.site.register(OTHR_EMPLY_BNFT)
from .bird_data_model import OTHR_FNNCL_CLLTRL
admin.site.register(OTHR_FNNCL_CLLTRL)
from .bird_data_model import OTHR_FNNCL_CRPRTN
admin.site.register(OTHR_FNNCL_CRPRTN)
from .bird_data_model import OTHR_GRP_CLNTS
admin.site.register(OTHR_GRP_CLNTS)
from .bird_data_model import OTHR_IMMTRL_RGHTS_CLLTRL
admin.site.register(OTHR_IMMTRL_RGHTS_CLLTRL)
from .bird_data_model import OTC_INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT
admin.site.register(OTC_INSTRMNT_CLLTRL_RCVD_INSTRMNT_ASSGNMNT)
from .bird_data_model import OTHR_INTNGL_ASST
admin.site.register(OTHR_INTNGL_ASST)
from .bird_data_model import OTHR_INTNGBL_ASST_NT_TKN_INT_PSSSSN
admin.site.register(OTHR_INTNGBL_ASST_NT_TKN_INT_PSSSSN)
from .bird_data_model import OTHR_INTNGBL_ASST_TKN_INT_PSSSSN
admin.site.register(OTHR_INTNGBL_ASST_TKN_INT_PSSSSN)
from .bird_data_model import OTHR_LN
admin.site.register(OTHR_LN)
from .bird_data_model import OTHR_LN_CRDTR_ASSGNMNT
admin.site.register(OTHR_LN_CRDTR_ASSGNMNT)
from .bird_data_model import OTHR_LN_DBTR_ASSGNMNT
admin.site.register(OTHR_LN_DBTR_ASSGNMNT)
from .bird_data_model import OTHR_NN_FNNCL_ASST
admin.site.register(OTHR_NN_FNNCL_ASST)
from .bird_data_model import OTHR_NN_FNNCL_ASST_NT_TKN_INT_PSSSSN
admin.site.register(OTHR_NN_FNNCL_ASST_NT_TKN_INT_PSSSSN)
from .bird_data_model import OTHR_NN_FNNCL_ASST_TKN_INT_PSSSSN_BFR_PRD
admin.site.register(OTHR_NN_FNNCL_ASST_TKN_INT_PSSSSN_BFR_PRD)
from .bird_data_model import OTHR_NN_FNNCL_ASST_TKN_INT_PSSSSN_DRNG_PRD
admin.site.register(OTHR_NN_FNNCL_ASST_TKN_INT_PSSSSN_DRNG_PRD)
from .bird_data_model import OTHR_NN_FNNCL_LBLTY
admin.site.register(OTHR_NN_FNNCL_LBLTY)
from .bird_data_model import OTHR_NN_RGSTRD_CLLTRL
admin.site.register(OTHR_NN_RGSTRD_CLLTRL)
from .bird_data_model import OTHR_ORGNSTNL_UNT
admin.site.register(OTHR_ORGNSTNL_UNT)
from .bird_data_model import OTHR_OVRNGHT_DPST
admin.site.register(OTHR_OVRNGHT_DPST)
from .bird_data_model import OTHR_OTC_DRVTV_INSTRMNT
admin.site.register(OTHR_OTC_DRVTV_INSTRMNT)
from .bird_data_model import OTHR_OTC_SWP
admin.site.register(OTHR_OTC_SWP)
from .bird_data_model import OTHR_PRTY_CD
admin.site.register(OTHR_PRTY_CD)
from .bird_data_model import OTHR_PRTY_ID
admin.site.register(OTHR_PRTY_ID)
from .bird_data_model import OTHR_PRVSN
admin.site.register(OTHR_PRVSN)
from .bird_data_model import OTHR_TRD_RCVBL
admin.site.register(OTHR_TRD_RCVBL)
from .bird_data_model import OVRNGHT_DPST
admin.site.register(OVRNGHT_DPST)
from .bird_data_model import OTC_CDS
admin.site.register(OTC_CDS)
from .bird_data_model import OTC_CRDT_DFLT_SWP_CLLTRL_RCVD_INSTRMNT_ASSGNMNT
admin.site.register(OTC_CRDT_DFLT_SWP_CLLTRL_RCVD_INSTRMNT_ASSGNMNT)
from .bird_data_model import OTC_SRDT_DFLT_SWP_RCVD_CLLTRL_INSTRMNT
admin.site.register(OTC_SRDT_DFLT_SWP_RCVD_CLLTRL_INSTRMNT)
from .bird_data_model import OTC_CRDT_SPRD_OPTN
admin.site.register(OTC_CRDT_SPRD_OPTN)
from .bird_data_model import OTC_DRVTV_HDG
admin.site.register(OTC_DRVTV_HDG)
from .bird_data_model import OTC_DRVTV_BUYR_ASSGNMNT
admin.site.register(OTC_DRVTV_BUYR_ASSGNMNT)
from .bird_data_model import OTC_DRVTV_INSTRMNT
admin.site.register(OTC_DRVTV_INSTRMNT)
from .bird_data_model import OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT
admin.site.register(OTC_DRVTV_INSTRMNT_SNTHTC_SCRTSTN_ASSGNMNT)
from .bird_data_model import OTC_DRVTV_RL
admin.site.register(OTC_DRVTV_RL)
from .bird_data_model import OTC_DRVTV_SLLR_ASSGNMNT
admin.site.register(OTC_DRVTV_SLLR_ASSGNMNT)
from .bird_data_model import OTC_FRWRD
admin.site.register(OTC_FRWRD)
from .bird_data_model import OTC_OPTN
admin.site.register(OTC_OPTN)
from .bird_data_model import OTHR_OTC_OPTN
admin.site.register(OTHR_OTC_OPTN)
from .bird_data_model import OTC_SWP
admin.site.register(OTC_SWP)
from .bird_data_model import OTC_TTL_RTRN_SWP
admin.site.register(OTC_TTL_RTRN_SWP)
from .bird_data_model import PRTNR_ENTRPRS
admin.site.register(PRTNR_ENTRPRS)
from .bird_data_model import PRTNR_ENTRPRS_ASSGNMNT
admin.site.register(PRTNR_ENTRPRS_ASSGNMNT)
from .bird_data_model import PRTY
admin.site.register(PRTY)
from .bird_data_model import PRTY_CD
admin.site.register(PRTY_CD)
from .bird_data_model import PRTY_DRVD_DT
admin.site.register(PRTY_DRVD_DT)
from .bird_data_model import PRTY_PRVS_PRD_DT
admin.site.register(PRTY_PRVS_PRD_DT)
from .bird_data_model import PRTY_RSK_DT
admin.site.register(PRTY_RSK_DT)
from .bird_data_model import PRTY_RL
admin.site.register(PRTY_RL)
from .bird_data_model import PST_DU_FNNCL_ASST_INSTRMNT
admin.site.register(PST_DU_FNNCL_ASST_INSTRMNT)
from .bird_data_model import PNDNG_LGL_ISSS_TX_LTGTN
admin.site.register(PNDNG_LGL_ISSS_TX_LTGTN)
from .bird_data_model import PNSN_OTHR_PST_EMPLYMNT_BNFT_OBLGTN
admin.site.register(PNSN_OTHR_PST_EMPLYMNT_BNFT_OBLGTN)
from .bird_data_model import PRFRMNG_DBT_SCRTY
admin.site.register(PRFRMNG_DBT_SCRTY)
from .bird_data_model import PRFRMNG_FNNCL_ASST_INSTRMNT_DBTR_ASSSSD
admin.site.register(PRFRMNG_FNNCL_ASST_INSTRMNT_DBTR_ASSSSD)
from .bird_data_model import PRFRMNG_NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD
admin.site.register(PRFRMNG_NN_DFLT_FNNCL_ASST_INSTRMNT_INDVDLLY_ASSSSD)
from .bird_data_model import PRFRMNG_NN_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT
admin.site.register(PRFRMNG_NN_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT)
from .bird_data_model import PRPTL_DBT_SCRTY
admin.site.register(PRPTL_DBT_SCRTY)
from .bird_data_model import PHYSCL_CLLTRL
admin.site.register(PHYSCL_CLLTRL)
from .bird_data_model import PHYSCL_CLLTRL_INVSTMNT_PRPRTY_ASSGNMNT
admin.site.register(PHYSCL_CLLTRL_INVSTMNT_PRPRTY_ASSGNMNT)
from .bird_data_model import PHYSCL_CLLTRL_NN_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(PHYSCL_CLLTRL_NN_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import PHYSCL_CLLTRL_NN_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(PHYSCL_CLLTRL_NN_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import PTNTL_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT
admin.site.register(PTNTL_RTL_EXPSR_CLSS_FNNCL_ASST_INSTRMNT)
from .bird_data_model import PRVT_SCTR_CMPNY_OTHR_THN_CRPRTN
admin.site.register(PRVT_SCTR_CMPNY_OTHR_THN_CRPRTN)
from .bird_data_model import PRPRTY_PLNT_EQPMNT
admin.site.register(PRPRTY_PLNT_EQPMNT)
from .bird_data_model import PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN
admin.site.register(PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN)
from .bird_data_model import PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN
admin.site.register(PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN)
from .bird_data_model import PRTCTN_ARRNGMNT
admin.site.register(PRTCTN_ARRNGMNT)
from .bird_data_model import PRTCTN_PRTCTN_PRVD_ASSGNMNT
admin.site.register(PRTCTN_PRTCTN_PRVD_ASSGNMNT)
from .bird_data_model import PRTCTN_PRVDR
admin.site.register(PRTCTN_PRVDR)
from .bird_data_model import PRVSN
admin.site.register(PRVSN)
from .bird_data_model import PRDNTL_CNSLDTN_GRP
admin.site.register(PRDNTL_CNSLDTN_GRP)
from .bird_data_model import QCCP
admin.site.register(QCCP)
from .bird_data_model import RTNG_AGNCY
admin.site.register(RTNG_AGNCY)
from .bird_data_model import RTNG_GRD
admin.site.register(RTNG_GRD)
from .bird_data_model import RTNG_GRD_CNTRY_ASSGNMNT
admin.site.register(RTNG_GRD_CNTRY_ASSGNMNT)
from .bird_data_model import RTNG_GRD_ISS_BSD_RTNG_SYSTM
admin.site.register(RTNG_GRD_ISS_BSD_RTNG_SYSTM)
from .bird_data_model import RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT
admin.site.register(RTNG_GRD_ISS_BSD_RTNG_SSTM_DBT_SCRTY_ASSGNMNT)
from .bird_data_model import RTNG_GRD_ISSR_BSD_RTNG_SYSTM
admin.site.register(RTNG_GRD_ISSR_BSD_RTNG_SYSTM)
from .bird_data_model import RTNG_GRD_ISSR_BSD_RTNG_SYSTM_CNTRL_GVRNMNT
admin.site.register(RTNG_GRD_ISSR_BSD_RTNG_SYSTM_CNTRL_GVRNMNT)
from .bird_data_model import RTNG_GRD_ISSR_BSD_RTNG_SYSTM_NN_CNTRL_GVRNMNT
admin.site.register(RTNG_GRD_ISSR_BSD_RTNG_SYSTM_NN_CNTRL_GVRNMNT)
from .bird_data_model import RTNG_GRD_OTHR_ORGNSTN_ASSGNMNT
admin.site.register(RTNG_GRD_OTHR_ORGNSTN_ASSGNMNT)
from .bird_data_model import RTNG_SYSTM
admin.site.register(RTNG_SYSTM)
from .bird_data_model import RTNG_SYSTM_APPLD_LGL_PRSN
admin.site.register(RTNG_SYSTM_APPLD_LGL_PRSN)
from .bird_data_model import RL_ESTT_CLLTRL
admin.site.register(RL_ESTT_CLLTRL)
from .bird_data_model import RL_ESTT_CLLTRL_LCTD_MMBR_STT
admin.site.register(RL_ESTT_CLLTRL_LCTD_MMBR_STT)
from .bird_data_model import RL_ESTT_CLLTRL_NT_LCTD_MMBR_STT
admin.site.register(RL_ESTT_CLLTRL_NT_LCTD_MMBR_STT)
from .bird_data_model import RGSTRD_CLLTRL
admin.site.register(RGSTRD_CLLTRL)
from .bird_data_model import UPU_SYSTM_PRTY
admin.site.register(UPU_SYSTM_PRTY)
from .bird_data_model import RIAD_PRTY_CD
admin.site.register(RIAD_PRTY_CD)
from .bird_data_model import RNGTTD_FNNCL_ASST_INSTRMNT
admin.site.register(RNGTTD_FNNCL_ASST_INSTRMNT)
from .bird_data_model import RNGTTD_FNNCL_ASST_INSTRMNT_WTH_FRBRNC_MSR
admin.site.register(RNGTTD_FNNCL_ASST_INSTRMNT_WTH_FRBRNC_MSR)
from .bird_data_model import RNGTTD_FNNCL_ASST_INSTRMNT_FRBRNC_MSR_DRVD_DT
admin.site.register(RNGTTD_FNNCL_ASST_INSTRMNT_FRBRNC_MSR_DRVD_DT)
from .bird_data_model import RNGTTD_FNNCL_ASST_INSTRMNT_WTHT_FRBRNC_MSR
admin.site.register(RNGTTD_FNNCL_ASST_INSTRMNT_WTHT_FRBRNC_MSR)
from .bird_data_model import RPRTNG_AGNT_INTRNL_GRP_RL
admin.site.register(RPRTNG_AGNT_INTRNL_GRP_RL)
from .bird_data_model import RPRCHS_AGRMNT_BYR_ASSGNMNT
admin.site.register(RPRCHS_AGRMNT_BYR_ASSGNMNT)
from .bird_data_model import RPRCHS_AGRMNT_CMPNNT
admin.site.register(RPRCHS_AGRMNT_CMPNNT)
from .bird_data_model import RPRCHS_AGRMNT_INSTRMNT
admin.site.register(RPRCHS_AGRMNT_INSTRMNT)
from .bird_data_model import RPRCHS_AGRMNT_SLLR_ASSGNMNT
admin.site.register(RPRCHS_AGRMNT_SLLR_ASSGNMNT)
from .bird_data_model import RSDNTL_RL_ESTT_CLLTRL
admin.site.register(RSDNTL_RL_ESTT_CLLTRL)
from .bird_data_model import RSTRCTRNG
admin.site.register(RSTRCTRNG)
from .bird_data_model import RSK_FAC_SA
admin.site.register(RSK_FAC_SA)
from .bird_data_model import KB_PR_BCKT
admin.site.register(KB_PR_BCKT)
from .bird_data_model import RLLNG_STCK_CLLTRL
admin.site.register(RLLNG_STCK_CLLTRL)
from .bird_data_model import SFT
admin.site.register(SFT)
from .bird_data_model import SCRTSTN
admin.site.register(SCRTSTN)
from .bird_data_model import SCRTSN_OTHR_CRDT_TRNSFR
admin.site.register(SCRTSN_OTHR_CRDT_TRNSFR)
from .bird_data_model import SCRTSTN_CRRLTN_TRDNG_PRTFL_RSK_FCTR_STNDRDSD_APPRCH
admin.site.register(SCRTSTN_CRRLTN_TRDNG_PRTFL_RSK_FCTR_STNDRDSD_APPRCH)
from .bird_data_model import SCRTSTN_NN_CRRLTN_TRDNG_PRTFL_RSK_FCTR_FR_STNDRDSD_APPRCH
admin.site.register(SCRTSTN_NN_CRRLTN_TRDNG_PRTFL_RSK_FCTR_FR_STNDRDSD_APPRCH)
from .bird_data_model import SSPE
admin.site.register(SSPE)
from .bird_data_model import SCRTSTN_TRNCH
admin.site.register(SCRTSTN_TRNCH)
from .bird_data_model import SCRTY
admin.site.register(SCRTY)
from .bird_data_model import SCRTY_AGNST_F_BRRWNG_LNDNG_TRNSCTN
admin.site.register(SCRTY_AGNST_F_BRRWNG_LNDNG_TRNSCTN)
from .bird_data_model import SCRTY_AGNST_SCRTY_BRRWNG_LNDNG_TRNSCTN
admin.site.register(SCRTY_AGNST_SCRTY_BRRWNG_LNDNG_TRNSCTN)
from .bird_data_model import SCRTY_EXCHNG_TRDBL_DRVTV
admin.site.register(SCRTY_EXCHNG_TRDBL_DRVTV)
from .bird_data_model import SCRTY_BRRWNG_LNDNG_TRNSCTN
admin.site.register(SCRTY_BRRWNG_LNDNG_TRNSCTN)
from .bird_data_model import SCRTY_BRRWNG_LNDNG_TRNSCTN_BRRWR_ASSGNMNT
admin.site.register(SCRTY_BRRWNG_LNDNG_TRNSCTN_BRRWR_ASSGNMNT)
from .bird_data_model import SCRTY_BRRWNG_LNDNG_TRNSCTN_CSH_CLLTRL
admin.site.register(SCRTY_BRRWNG_LNDNG_TRNSCTN_CSH_CLLTRL)
from .bird_data_model import SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT
admin.site.register(SCRTY_BRRWNG_LNDNG_TRNSCTN_CMPNNT)
from .bird_data_model import SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL
admin.site.register(SCTRY_BRRWNG_LNDNG_TRNSCTN_INCLDNG_CSH_CLLTRL)
from .bird_data_model import SCRTY_BRRWNG_LNDNG_TRNSCTN_LNDR_ASSGNMNT
admin.site.register(SCRTY_BRRWNG_LNDNG_TRNSCTN_LNDR_ASSGNMNT)
from .bird_data_model import SCRTY_BRRWNG_CMPNNT
admin.site.register(SCRTY_BRRWNG_CMPNNT)
from .bird_data_model import SCRTY_CLLTRL
admin.site.register(SCRTY_CLLTRL)
from .bird_data_model import SCRTY_DBTR
admin.site.register(SCRTY_DBTR)
from .bird_data_model import SCRTY_DRVD_DT
admin.site.register(SCRTY_DRVD_DT)
from .bird_data_model import SCRTY_ENTTY_RL_ASSGNMNT
admin.site.register(SCRTY_ENTTY_RL_ASSGNMNT)
from .bird_data_model import SCRTY_ISSR_ASSGNMNT
admin.site.register(SCRTY_ISSR_ASSGNMNT)
from .bird_data_model import SCRTY_LG
admin.site.register(SCRTY_LG)
from .bird_data_model import SCRTY_LNDNG_CMPNNT
admin.site.register(SCRTY_LNDNG_CMPNNT)
from .bird_data_model import SCRTY_EXCHNG_TRDBL_DRVTV_PSTN
admin.site.register(SCRTY_EXCHNG_TRDBL_DRVTV_PSTN)
from .bird_data_model import SCRTY_PSTN
admin.site.register(SCRTY_PSTN)
from .bird_data_model import SCRTY_PSTN_DRVD_DT
admin.site.register(SCRTY_PSTN_DRVD_DT)
from .bird_data_model import SCRTY_HDGD_EXCHNG_TRDBL_DRVTV
admin.site.register(SCRTY_HDGD_EXCHNG_TRDBL_DRVTV)
from .bird_data_model import SCRTY_PSTN_HDGD_OTC_DRVTV
admin.site.register(SCRTY_PSTN_HDGD_OTC_DRVTV)
from .bird_data_model import SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT
admin.site.register(SCRTY_SCRTY_RPRCHS_AGRMNT_CMPNNT_ASSGNMNT)
from .bird_data_model import SLF_EMPLYD_NTRL_PRSN
admin.site.register(SLF_EMPLYD_NTRL_PRSN)
from .bird_data_model import SLLR
admin.site.register(SLLR)
from .bird_data_model import SRVCR
admin.site.register(SRVCR)
from .bird_data_model import SHR_CPTL_RPYBL_DMND
admin.site.register(SHR_CPTL_RPYBL_DMND)
from .bird_data_model import SHP_CLLTRL
admin.site.register(SHP_CLLTRL)
from .bird_data_model import SHRT_SCRTY_PSTN_BNKG_BK
admin.site.register(SHRT_SCRTY_PSTN_BNKG_BK)
from .bird_data_model import SHRT_SCRTY_PSTN
admin.site.register(SHRT_SCRTY_PSTN)
from .bird_data_model import SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
admin.site.register(SHRT_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT)
from .bird_data_model import SHRT_SCRTY_PSTN_TRDNG_BK
admin.site.register(SHRT_SCRTY_PSTN_TRDNG_BK)
from .bird_data_model import SHRT_SCRTY_PSTN_TRDNG_BK_DRVD_DT
admin.site.register(SHRT_SCRTY_PSTN_TRDNG_BK_DRVD_DT)
from .bird_data_model import SHRT_SCRTY_PSTN_TRDNG_BK_IFRS
admin.site.register(SHRT_SCRTY_PSTN_TRDNG_BK_IFRS)
from .bird_data_model import SHRT_SCRTY_PSTN_TRDNG_BK_NGAAP
admin.site.register(SHRT_SCRTY_PSTN_TRDNG_BK_NGAAP)
from .bird_data_model import SGNFCNT_RSK_TRNSFR_SCRTSTN
admin.site.register(SGNFCNT_RSK_TRNSFR_SCRTSTN)
from .bird_data_model import SGNFCNT_RSK_TRNSFR_SCRTSTN_DRVD_DT
admin.site.register(SGNFCNT_RSK_TRNSFR_SCRTSTN_DRVD_DT)
from .bird_data_model import SNGL_FNNCL_CNTRCT
admin.site.register(SNGL_FNNCL_CNTRCT)
from .bird_data_model import SFTWR_CLLTRL
admin.site.register(SFTWR_CLLTRL)
from .bird_data_model import SFTWR_CLLTRL_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(SFTWR_CLLTRL_SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import SFTWR_CLLTRL_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(SFTWR_CLLTRL_SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(SFTWR_PPRTY_PLNT_EQPMNT_NT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT
admin.site.register(SFTWR_PPRTY_PLNT_EQPMNT_TKN_INT_PSSSSN_ASSGNMNT)
from .bird_data_model import SPNSR
admin.site.register(SPNSR)
from .bird_data_model import STT_LCL_GVRNMNT_SCL_SCRTY_FNDS
admin.site.register(STT_LCL_GVRNMNT_SCL_SCRTY_FNDS)
from .bird_data_model import SBSDRY_JNT_VNTR_ASSCT
admin.site.register(SBSDRY_JNT_VNTR_ASSCT)
from .bird_data_model import SBSDRY_JNT_VNTR_ASSCT_ASSCT_ASSGNMNT
admin.site.register(SBSDRY_JNT_VNTR_ASSCT_ASSCT_ASSGNMNT)
from .bird_data_model import SBSDRY_JNT_VNTR_ASSCT_JNT_VNTR_ASSGNMNT
admin.site.register(SBSDRY_JNT_VNTR_ASSCT_JNT_VNTR_ASSGNMNT)
from .bird_data_model import SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT
admin.site.register(SBSDRY_JNT_VNTR_ASSCT_OTHR_ORGNSTN_ASSGNMNT)
from .bird_data_model import SBSDRY_JNT_VNTR_ASSCT_SBSDRY_ASSGNMNT
admin.site.register(SBSDRY_JNT_VNTR_ASSCT_SBSDRY_ASSGNMNT)
from .bird_data_model import SBSDRY
admin.site.register(SBSDRY)
from .bird_data_model import SSPNS_ITM
admin.site.register(SSPNS_ITM)
from .bird_data_model import SWP_PRVDR
admin.site.register(SWP_PRVDR)
from .bird_data_model import SYNDCTD_CNTRCT
admin.site.register(SYNDCTD_CNTRCT)
from .bird_data_model import SYNDCTD_FNNCL_CNTRCT_MMBR
admin.site.register(SYNDCTD_FNNCL_CNTRCT_MMBR)
from .bird_data_model import SNTHTC_SCRTSTN
admin.site.register(SNTHTC_SCRTSTN)
from .bird_data_model import SYNTHTC_SCRTSTN_SSPE
admin.site.register(SYNTHTC_SCRTSTN_SSPE)
from .bird_data_model import SYNTHTC_SCRTSTN_WTHT_SSPE
admin.site.register(SYNTHTC_SCRTSTN_WTHT_SSPE)
from .bird_data_model import TS_ASST
admin.site.register(TS_ASST)
from .bird_data_model import TX_LBLTY
admin.site.register(TX_LBLTY)
from .bird_data_model import TRM_RPRCHS_AGRMNT_INSTRMNT
admin.site.register(TRM_RPRCHS_AGRMNT_INSTRMNT)
from .bird_data_model import TRD_RCVBL
admin.site.register(TRD_RCVBL)
from .bird_data_model import TRD_RCVBL_ASSGND_DBTR_ASSGNMNT
admin.site.register(TRD_RCVBL_ASSGND_DBTR_ASSGNMNT)
from .bird_data_model import TRD_RCVBL_CLLTRL
admin.site.register(TRD_RCVBL_CLLTRL)
from .bird_data_model import TRD_RCBVBL_FCTR_ASSGNMNT
admin.site.register(TRD_RCBVBL_FCTR_ASSGNMNT)
from .bird_data_model import TRDTNL_SCRTSTN
admin.site.register(TRDTNL_SCRTSTN)
from .bird_data_model import TRNCH_SYNTHTC_SCRTSTN
admin.site.register(TRNCH_SYNTHTC_SCRTSTN)
from .bird_data_model import TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE
admin.site.register(TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE)
from .bird_data_model import TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST
admin.site.register(TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_DPST)
from .bird_data_model import TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT
admin.site.register(TRNCH_SYNTHTC_SCRTSTN_WTHT_SSPE_FNNCL_GRNT)
from .bird_data_model import TRNCH_SYNTHTC_SCRTSTN_SCRTSTN_SPCL_PRPS_ENTTY
admin.site.register(TRNCH_SYNTHTC_SCRTSTN_SCRTSTN_SPCL_PRPS_ENTTY)
from .bird_data_model import TRNCH_TRDTNL_SCRTSTN
admin.site.register(TRNCH_TRDTNL_SCRTSTN)
from .bird_data_model import TRNSFRBL_DPST
admin.site.register(TRNSFRBL_DPST)
from .bird_data_model import TRNSFRD_ASST_LG
admin.site.register(TRNSFRD_ASST_LG)
from .bird_data_model import TRNST_ITM
admin.site.register(TRNST_ITM)
from .bird_data_model import VG_SNSTVTY
admin.site.register(VG_SNSTVTY)
from .bird_data_model import Balance_sheet_recognised_financial_asset_instrument_type
admin.site.register(Balance_sheet_recognised_financial_asset_instrument_type)
from .bird_data_model import Balance_sheet_recognised_financial_asset_instrument_by_fair_value_type
admin.site.register(Balance_sheet_recognised_financial_asset_instrument_by_fair_value_type)
from .bird_data_model import Balance_sheet_recognised_financial_liability_instrument_type
admin.site.register(Balance_sheet_recognised_financial_liability_instrument_type)
from .bird_data_model import Balance_sheet_recognised_financial_liability_instrument_accounting_standard
admin.site.register(Balance_sheet_recognised_financial_liability_instrument_accounting_standard)
from .bird_data_model import Central_bank_and_private_sector_company_type
admin.site.register(Central_bank_and_private_sector_company_type)
from .bird_data_model import Listed_central_bank_and_private_sector_company_indicator
admin.site.register(Listed_central_bank_and_private_sector_company_indicator)
from .bird_data_model import Collateral_type
admin.site.register(Collateral_type)
from .bird_data_model import Obtained_collateral_type
admin.site.register(Obtained_collateral_type)
from .bird_data_model import Collateral_received_instrument_type
admin.site.register(Collateral_received_instrument_type)
from .bird_data_model import Obtained_collateral_received_instrument_type
admin.site.register(Obtained_collateral_received_instrument_type)
from .bird_data_model import Debt_security_type
admin.site.register(Debt_security_type)
from .bird_data_model import Debt_security_by_Performing_status_type
admin.site.register(Debt_security_by_Performing_status_type)
from .bird_data_model import Perpetual_debt_security_indicator
admin.site.register(Perpetual_debt_security_indicator)
from .bird_data_model import Debt_security_by_accounting_standard
admin.site.register(Debt_security_by_accounting_standard)
from .bird_data_model import Debt_security_issued_type
admin.site.register(Debt_security_issued_type)
from .bird_data_model import Debt_security_issued_prudential_portfolio_type
admin.site.register(Debt_security_issued_prudential_portfolio_type)
from .bird_data_model import Entity_role_typev1
admin.site.register(Entity_role_typev1)
from .bird_data_model import Entity_role_type
admin.site.register(Entity_role_type)
from .bird_data_model import Financial_asset_instrument_type_by_renegotiation_status
admin.site.register(Financial_asset_instrument_type_by_renegotiation_status)
from .bird_data_model import Financial_asset_instrument_type_by_fixed_interest_rate
admin.site.register(Financial_asset_instrument_type_by_fixed_interest_rate)
from .bird_data_model import Financial_asset_instrument_type_by_CRR_Article_123_Retail_exposure
admin.site.register(Financial_asset_instrument_type_by_CRR_Article_123_Retail_exposure)
from .bird_data_model import Financial_asset_instrument_type_by_interest_rate_only
admin.site.register(Financial_asset_instrument_type_by_interest_rate_only)
from .bird_data_model import Financial_asset_instrument_type
admin.site.register(Financial_asset_instrument_type)
from .bird_data_model import Past_due_financial_asset_instrument_indicator
admin.site.register(Past_due_financial_asset_instrument_indicator)
from .bird_data_model import Risk_measure_type
admin.site.register(Risk_measure_type)
from .bird_data_model import Risk_measure_type_by_position
admin.site.register(Risk_measure_type_by_position)
from .bird_data_model import Instrument_type_by_origin
admin.site.register(Instrument_type_by_origin)
from .bird_data_model import Instrument_type_by_product
admin.site.register(Instrument_type_by_product)
from .bird_data_model import Long_security_position_type
admin.site.register(Long_security_position_type)
from .bird_data_model import Negotiable_security_position_indicator
admin.site.register(Negotiable_security_position_indicator)
from .bird_data_model import Long_security_position_Prudential_portfolio_assignment_type
admin.site.register(Long_security_position_Prudential_portfolio_assignment_type)
from .bird_data_model import Long_security_position_Prudential_portfolio_type
admin.site.register(Long_security_position_Prudential_portfolio_type)
from .bird_data_model import Organisation_type
admin.site.register(Organisation_type)
from .bird_data_model import Organisation_type_by_legal_proceeding_status
admin.site.register(Organisation_type_by_legal_proceeding_status)
from .bird_data_model import Party_type_by_address
admin.site.register(Party_type_by_address)
from .bird_data_model import Party_type
admin.site.register(Party_type)
from .bird_data_model import Property_plant_and_equipment_type
admin.site.register(Property_plant_and_equipment_type)
from .bird_data_model import Software_assets_indicator
admin.site.register(Software_assets_indicator)
from .bird_data_model import Rating_system_type_by_nature_Grade_vs_Numeric
admin.site.register(Rating_system_type_by_nature_Grade_vs_Numeric)
from .bird_data_model import Rating_system_type_by_target_Issue_vs_Issuer_based
admin.site.register(Rating_system_type_by_target_Issue_vs_Issuer_based)
from .bird_data_model import Real_estate_collateral_location_type
admin.site.register(Real_estate_collateral_location_type)
from .bird_data_model import Real_estate_collateral_type
admin.site.register(Real_estate_collateral_type)
from .bird_data_model import Securitisation_type
admin.site.register(Securitisation_type)
from .bird_data_model import Significant_risk_transfer_indicator
admin.site.register(Significant_risk_transfer_indicator)
from .bird_data_model import Security_type_by_product
admin.site.register(Security_type_by_product)
from .bird_data_model import Security_type_by_identifier
admin.site.register(Security_type_by_identifier)
from .bird_data_model import Security_borrowing_and_lending_transaction_component_type_by_Security_type
admin.site.register(Security_borrowing_and_lending_transaction_component_type_by_Security_type)
from .bird_data_model import Security_borrowing_and_lending_transaction_component_type_by_direction
admin.site.register(Security_borrowing_and_lending_transaction_component_type_by_direction)

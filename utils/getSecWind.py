from WindPy import *
import datetime
import pandas as pd
import numpy as np

def getAllSec_AShare(date=None):
    if date is None:
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
    w.start()
    data = w.wset("sectorconstituent", "date={0};sectorid=a001010100000000".format(date))
    result = pd.DataFrame({
        'wind_code': data.Data[1],
        'sec_name': data.Data[2]
    })
    w.close()
    return(result)

def getIncomeSheet(security, date, isQuarter=False):
    """
    get all numbers in income sheet
    :param security:
    :param date: shoud be in the format of YYYY
    :return:
    """
    w.start()
    all_income_sheet_items = "Insur_rsrv_recoverable,reinsur_exp_recoverable," \
                             "other_oper_exp,net_inc_other_ops,net_gain_chg_fv," \
                             "net_invest_inc,inc_invest_assoc_jv_entp,net_gain_fx_trans," \
                             "opprofit,non_oper_rev,non_oper_exp,net_loss_disp_noncur_asset," \
                             "tot_profit,tax,unconfirmed_invest_loss_is,net_profit_is,minority_int_inc," \
                             "np_belongto_parcomsh,other_compreh_inc,tot_compreh_inc,tot_compreh_inc_min_shrhldr," \
                             "tot_compreh_inc_parent_comp"
    all_qtr_income_sheet_items = "qfa_tot_oper_rev,qfa_oper_rev,qfa_interest_inc,qfa_insur_prem_unearned,qfa_handling_chrg_comm_inc,qfa_tot_prem_inc,qfa_reinsur_inc,qfa_prem_ceded,qfa_unearned_prem_rsrv,qfa_net_inc_agency business,qfa_net_inc_underwriting-business,qfa_net_inc_customerasset-management business,qfa_other_oper_inc,qfa_net_int_inc,qfa_net_fee_and_commission_inc,qfa_net_other_oper_inc,qfa_tot_oper_cost,qfa_oper_cost,qfa_grossmargin,qfa_interest_exp,qfa_handling_chrg_comm_exp,qfa_oper_exp,qfa_taxes_surcharges_ops,qfa_selling_dist_exp,qfa_gerl_admin_exp,qfa_fin_exp_is,qfa_impair_loss_assets,qfa_prepay_surr,qfa_net_claim_exp,qfa_net_insur_cont_rsrv,qfa_dvd_exp_insured,qfa_reinsurance_exp,qfa_claim_exp_recoverable,qfa_Insur_rsrv_recoverable,qfa_reinsur_exp_recoverable,qfa_other_oper_exp,qfa_net_gain_chg_fv,qfa_net_invest_inc,qfa_inc_invest_assoc_jv_entp,qfa_net_gain_fx_trans,qfa_opprofit,qfa_non_oper_rev,qfa_non_oper_exp,qfa_net_loss_disp_noncur_asset,qfa_tot_profit,qfa_tax,qfa_unconfirmed_invest_loss_is,qfa_net_profit_is,qfa_minority_int_inc,qfa_np_belongto_parcomsh,qfa_other_compreh_inc,qfa_tot_compreh_inc,qfa_tot_compreh_inc_min_shrhldr,qfa_tot_compreh_inc_parent_comp"

    if not isQuarter:
        code = all_income_sheet_items
    else:
        code = all_qtr_income_sheet_items
    data = w.wss(security, code, "unit=1;rptDate={0};rptType=1".format(date))
    result = set()
    for d in data.Data:
        if d[0] != None and not np.isnan(d[0]) and d[0] > 0 :
            result.add(d[0])
    return(list(result))

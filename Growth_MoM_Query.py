from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

def income_statement_name(income_statement):
    return f"select '{income_statement}' as `Income Statement`,"

def column_creation_query(tran_month,columns,concat_exec = True):
    current_date = datetime.strptime(str(tran_month) + "-01","%Y%m-%d")
    previous_date = current_date - relativedelta(months=1)
    previous_tran_month = previous_date.strftime("%Y%m")
    current_month = calendar.month_name[int(tran_month % 100)]
    previous_month = calendar.month_name[int(previous_tran_month) % 100]
    year = int((round(tran_month / 100,0)) % 100)

    if concat_exec:
        concat_original_query= f"""SUM(CASE WHEN tran_month = {tran_month} THEN {columns}  ELSE 0 END) as  "{current_month}-{year}",CONCAT(ROUND(((SUM(CASE WHEN tran_month = {tran_month} THEN {columns} ELSE 0 END) - SUM(CASE WHEN tran_month = {previous_tran_month} THEN {columns} ELSE 0 END)) / NULLIF(SUM(CASE WHEN tran_month = {previous_tran_month} THEN {columns} ELSE 0 END),1)) * 100,2),"%") as `{current_month}{year} - {previous_month}{year} %`"""
        
        return concat_original_query  
    # Return the concatenated query if concat_exec is True. Otherwise, return the single query as a string.
    
    else:
        original_query = f"""SUM(CASE WHEN tran_month = {tran_month} THEN subtotal  ELSE 0 END) as  '{current_month}-{year}' """

        return original_query

def report_name(template_name):
    query = f"from {template_name} "
    return query

def conditions(condition_needed = False,*args):
    if condition_needed:
        return f"WHERE is_parsed = true and is_deleted= false and is_active = true and is_unqiue = true and {args}"
    else:
        return "WHERE is_parsed = true and is_deleted= false and is_active = true and is_unqiue = true"

def group_by(columns="",group_by_needed = False):
    if group_by_needed:
        query = f"group by {','.join(str(x) for x in columns)}"
        return query
    else:
        return ""
    
def order_by(columns="",order_by_needed = False):
    if order_by_needed:
        query = f"order by {','.join(str(x) for x in columns)}"
        return query
    else:
        return ""

def final_query_function(query_column_creation_params):
    final_query = ""

    for i in range(0,len(query_column_creation_params["KPI"])):
        for j in range(0, len(query_column_creation_params["tran_month"])):
            month = query_column_creation_params["tran_month"][j]
            kpi = query_column_creation_params["KPI"][i]
            column = query_column_creation_params["columns"][i]
            if month == query_column_creation_params["tran_month"][-1]:
                final_query = (income_statement_name(kpi) + final_query + column_creation_query(
                    month,column, concat_exec=False) + report_name(template_name = query_column_creation_params["report"]) +
                    conditions() + group_by(group_by_needed=False) + order_by(order_by_needed = False))
            else:
                final_query = final_query + column_creation_query(month,column, concat_exec=True)

        if  i == len(query_column_creation_params["KPI"]) - 1:
            final_query = final_query
            print(final_query)
        else:
            final_query = final_query+" UNION ALL "
            print(final_query)

    # for tran_month in final_list:
    #     final_query = final_query + column_creation_query(tran_month)
    #
    # final_query = income_statement_name(kpi) + final_query + column_creation_query(query_column_creation_params[0],concat_exec=False) + report_name(template_name = "doordash_rep") + conditions() + group_by(group_by_needed=False) + order_by(order_by_needed = False)
    return final_query


query_column_creation_params ={
    "KPI":["Total Sales","Doordash funded subtotal discount amount","Merchant Funded Discount","Commission"],
    "tran_month":[202411,202412,202501,202502,202503,202504,202505,202506,202507,202508,202509,202510,202511,202512],
    "columns" : ["subtotal","0 - (door_funde_subto_disco_amoun)","0 - (merc_funde_subto_disco_amoun)","0 - (commission)"],
    "report" :"doordash_rep",

}

query_column_creation_params["tran_month"] = query_column_creation_params["tran_month"][::-1]


print(final_query_function(query_column_creation_params))



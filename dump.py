query_column_creation_params ={
    "KPI":["Total Sales","Doordash funded subtotal discount amount","Merchant Funded Discount","Commission"],
    "tran_month":[202411,202412,202501,202502,202503,202504,202505,202506,202507,202508,202509,202510,202511,202512],
    "columns" : ["subtotal","0 - (door_funde_subto_disco_amoun)","0 - (merc_funde_subto_disco_amoun)","0 - (commission)"],
    "report" :"doordash_rep",

}

query_column_creation_params["tran_month"] = query_column_creation_params["tran_month"][::-1]

print(query_column_creation_params["tran_month"][-1])
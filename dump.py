dictionary = {
    'Income Statement' : ["total sales","Doordash funded subtotal discount amount","Merchant Funded Discount"],
    'tran_month':[202401,202402,202403,202404,202405],
    "columns":["total_sales","complex_amount"],

}

# for income_statement_keys in dictionary["Income Statement"]:
#     for tran_month_keys in dictionary["tran_month"]:
#         for column_keys in dictionary["columns"]:
#             print(income_statement_keys + "," + str(tran_month_keys)+"," + column_keys)


column1 = [202401,202402,202403,202404,202405]
print(", ".join(str(x) for x in column1))
def null_query(query_column_creation_params):
    """
    This function generates a null query based on the provided parameters.
    """
    query = "select" + " NULL ," * (((2 * (len(query_column_creation_params["tran_month"]))) - 1) - 1) + " NULL"

    return query

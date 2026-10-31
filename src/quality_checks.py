
import pandas as pd 


def get_data(data):
    if data is None:
        raise ValueError("Data is None.Please load data")
    return{
        "rows": len(data),
        "columns":len(data.columns)
    }

def check_missing_values(data):
    missing_values = data.isna().sum()
    missing_percentage = (missing_values / len(data)) * 100

    missing_table = pd.DataFrame({
        "missing_count":missing_values,
        "missing_percentage":missing_percentage
    })
    return missing_table


def duplicate_value(data):
    return int(data.duplicated().sum())

def get_numeric_values(data):

    numeric_data = data.select_dtypes(include=['number'])

    if numeric_data.empty:
        return {}
    
    return{
        "min": numeric_data.min(),
        "max": numeric_data.max(),
        "mean": numeric_data.mean(),
        "median": numeric_data.median()
    }

        





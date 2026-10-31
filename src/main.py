
from loader import load
import pandas as pd

from quality_checks import (
    get_data,
    check_missing_values,
    duplicate_value,
    get_numeric_values
)

from report import get_report

files = [
    "data/missing_Value.csv",
    "data/duplicate_rows.csv",
    "data/numeric_col.csv",
    "data/empty.csv",
    "data/unknown_car.csv"
]

for file_path in files:

    print("\nProcessing:", file_path)

    try:
        data = load(file_path)

        get_report(
            data,
            get_numeric_values,
            check_missing_values,
            duplicate_value,
            get_data
        )

    except pd.errors.EmptyDataError:
        print("Empty dataset. No data available.")

    except FileNotFoundError:
        print("File not found:", file_path)

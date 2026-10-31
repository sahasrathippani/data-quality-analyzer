
from loader import load
import pandas as pd
from pathlib import Path

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

Path("reports").mkdir(exist_ok=True)

for file_path in files:

    print("\nProcessing:", file_path)

    report_name = Path(file_path).stem + "_report.txt"
    report_path = Path("reports") / report_name

    try:
        data = load(file_path)

        if data.empty:
            raise pd.errors.EmptyDataError

        get_report(
            data,
            get_numeric_values,
            check_missing_values,
            duplicate_value,
            get_data,
            report_path
        )

    except pd.errors.EmptyDataError:
        message = "Empty dataset. No data available."
        print(message)
        report_path.write_text(message)

    except FileNotFoundError:
        message = f"File not found: {file_path}"
        print(message)
        report_path.write_text(message)

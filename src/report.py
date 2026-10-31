
import pandas as pd

def get_report(data, get_numeric_values, check_missing_values, duplicate_value, get_data):

    data_summary = get_data(data)
    missing_table = check_missing_values(data)
    numeric_summary = get_numeric_values(data)

    with open("report.txt", "w") as file:
        file.write("Data Quality Report\n")
        file.write("===================\n\n")

        file.write("DATASET INFORMATION\n")
        file.write("-" * 55 + "\n")
        file.write(f"Total Rows       : {data_summary['rows']}\n")
        file.write(f"Total Columns    : {data_summary['columns']}\n")
        file.write(f"Duplicate Rows   : {duplicate_value(data)}\n\n")

        file.write(f"Duplicate rows: {duplicate_value(data)}\n\n")

        file.write("Missing values:\n")
        file.write(missing_table.to_string())
        file.write("\n\n---------------\n")

        if numeric_summary:
            numeric_table = pd.DataFrame(numeric_summary)
            numeric_table.columns = ["Minimum", "Maximum", "Mean", "Median"]
            file.write(numeric_table.to_string())
        else:
            file.write("No numeric columns found.")

    print("Report generated successfully!")
    with open("report.txt", "r") as file:
        print(file.read())

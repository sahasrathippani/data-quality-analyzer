# Data Quality Analyzer

## Project Overview
Data Quality Analyzer is a Python-based project that analyzes CSV files and identifies common data quality issues using Pandas.

## Features
- Reads CSV files using Pandas.
- Displays the total number of rows and columns.
- Identifies missing values and calculates their percentages.
- Detects duplicate rows without deleting them.
- Calculates minimum, maximum, mean, and median for numeric columns.
- Handles empty datasets and missing files.
- Generates a data quality report.

## Technologies Used
- Python
- Pandas

## Testing
The project includes five test cases to verify missing values, duplicate rows, datasets without numeric columns, empty datasets, and missing files.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/main.py
```

Run the test cases:

```bash
python test/test_quality_checks.py
```

## Output
The project generates a data quality report containing dataset information, missing value analysis, duplicate row count, and numeric column statistics.
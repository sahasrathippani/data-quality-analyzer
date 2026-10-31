from pathlib import Path
import sys
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from loader import load
from quality_checks import (
    check_missing_values,
    duplicate_value,
    get_numeric_values
)

DATA = Path(__file__).resolve().parents[1] / "data"


# Test 1: Missing values
try:
    data = load(DATA / "missing_Value.csv")
    result = check_missing_values(data)

    assert result["missing_count"].sum() == 3
    print("Test 1: Missing values - PASSED")
except Exception as e:
    print("Test 1: FAILED -", e)


# Test 2: Duplicate rows
try:
    data = load(DATA / "duplicate_rows.csv")

    assert duplicate_value(data) == 1
    print("Test 2: Duplicate rows - PASSED")
except Exception as e:
    print("Test 2: FAILED -", e)


# Test 3: No numeric columns
try:
    data = load(DATA / "numeric_col.csv")

    assert get_numeric_values(data) == {}
    print("Test 3: No numeric columns - PASSED")
except Exception as e:
    print("Test 3: FAILED -", e)


# Test 4: Empty dataset
try:
    load(DATA / "empty.csv")
    print("Test 4: FAILED - Empty file was not detected")
except pd.errors.EmptyDataError:
    print("Test 4: Empty dataset - PASSED")
except Exception as e:
    print("Test 4: FAILED -", e)


# Test 5: Missing file
try:
    load(DATA / "unknown_car.csv")
    print("Test 5: FAILED - Missing file was not detected")
except FileNotFoundError:
    print("Test 5: Missing file - PASSED")
except Exception as e:
    print("Test 5: FAILED -", e)


print("\nAll five test cases completed.")
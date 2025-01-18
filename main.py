import pandas as pd

def analyze_file(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            return "Unsupported file format"

        # Check for missing data
        missing_data = df.isnull().sum().sum() > 0

        # Check for data type consistency
        inconsistent_types = False
        for col in df.columns:
            if df[col].apply(type).nunique() > 1:
                inconsistent_types = True
                break

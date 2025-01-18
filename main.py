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

# Check for duplicates
        duplicates = df.duplicated().any()

        # Check for outliers (simple example using z-score for numeric columns)
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if numeric_cols.any():
            z_scores = df[numeric_cols].apply(lambda x: (x - x.mean()) / x.std())
            outliers = (z_scores.abs() > 3).any().any()
        else:
            outliers = False

# Summary of checks
        summary = {
            "Missing Data": missing_data,
            "Inconsistent Types": inconsistent_types,
            "Duplicates": duplicates,
            "Outliers": outliers
        }
        
        return summary

    except Exception as e:
        return f"An error occurred: {str(e)}"

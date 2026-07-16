import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Loads the CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans column names for modeling and removes missing data."""
    df_clean = df.rename(columns={
        'Inflation_Rate (%)': 'Inflation',
        'GDP_Growth (%)': 'GDP_Growth'
    })
    # COUNTER-INTUITIVE CHOICE: We drop missing values entirely instead of filling them with averages.
    # Why? Filling macro-economic gaps with averages distorts the variance of natural economic shocks.
    return df_clean.dropna()

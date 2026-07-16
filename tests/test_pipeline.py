import pandas as pd
from src.data_prep import clean_data

def test_clean_data_unit():
    """Unit test: verifies column renaming and NA dropping."""
    df = pd.DataFrame({'Inflation_Rate (%)': [2.5, None], 'Petrol_Price_USD_per_Liter': [1.5, 1.6]})
    cleaned_df = clean_data(df)
    assert 'Inflation' in cleaned_df.columns
    assert len(cleaned_df) == 1

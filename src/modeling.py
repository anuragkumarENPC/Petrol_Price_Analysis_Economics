import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

def run_regression(df: pd.DataFrame):
    """Runs an OLS regression to determine drivers of petrol prices."""
    formula = "Petrol_Price_USD_per_Liter ~ Crude_Oil_Price_USD_per_Barrel + Inflation + GDP_Growth"
    return smf.ols(formula, data=df).fit()

def check_multicollinearity(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates Variance Inflation Factor (VIF) to check for feature correlation."""
    features = df[['Crude_Oil_Price_USD_per_Barrel', 'Inflation', 'GDP_Growth']].dropna()
    X = add_constant(features)
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
    return vif_data

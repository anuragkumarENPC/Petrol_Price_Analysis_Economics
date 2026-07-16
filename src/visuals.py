import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_crude_impact(df: pd.DataFrame) -> None:
    """Plots a scatter plot showing the relationship between crude oil and petrol prices."""
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df, x='Crude_Oil_Price_USD_per_Barrel', y='Petrol_Price_USD_per_Liter', color='teal', alpha=0.6)
    plt.title("Impact of Global Crude Oil on Pump Prices")
    plt.xlabel("Crude Oil (USD / Barrel)")
    plt.ylabel("Petrol Price (USD / Liter)")
    plt.show()

def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Plots a heatmap to visualize correlations between numeric macroeconomic variables."""
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title("Macroeconomic Correlation Heatmap")
    plt.tight_layout()
    plt.show()

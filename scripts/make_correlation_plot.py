import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

CLEAN_DIR = "data/clean/"
FIG_DIR = "figures/"

def main():

    df = pd.read_csv(os.path.join(CLEAN_DIR, "merged_clean.csv"))

    corr_cols = [
        "sp500_return",
        "gdp_growth",
        "cpi_inflation",
        "unemp_change",
        "indpro_growth",
        "retail_growth"
    ]

    corr = df[corr_cols].corr()

    # Ensure output directory exists
    os.makedirs(FIG_DIR, exist_ok=True)

    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix: S&P 500 Returns vs Macro Indicators")

    plt.savefig(os.path.join(FIG_DIR, "correlation_matrix.png"), dpi=300)
    plt.close()

    print("Correlation matrix saved to figures/correlation_matrix.png")

if __name__ == "__main__":
    main()

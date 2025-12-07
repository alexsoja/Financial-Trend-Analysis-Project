import pandas as pd
import statsmodels.api as sm
import os

CLEAN_DIR = "data/clean/"
RESULT_DIR = "results/"

def main():

    df = pd.read_csv(os.path.join(CLEAN_DIR, "merged_clean.csv"))

    # Regression variables
    X = df[[
        "gdp_growth",
        "cpi_inflation",
        "unemp_change",
        "indpro_growth",
        "retail_growth"
    ]]

    y = df["sp500_return"]

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # Ensure output folder exists
    os.makedirs(RESULT_DIR, exist_ok=True)

    # Save full summary to text file
    with open(os.path.join(RESULT_DIR, "regression_summary.txt"), "w") as f:
        f.write(model.summary().as_text())

    print("Regression summary saved to results/regression_summary.txt")

if __name__ == "__main__":
    main()

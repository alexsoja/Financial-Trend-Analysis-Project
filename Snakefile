import pandas as pd

RAW_DIR = "data/raw/"
CLEAN_DIR = "data/clean/"
FIG_DIR = "figures/"
RESULT_DIR = "results/"

rule all:
    input:
        CLEAN_DIR + "merged_clean.csv",
        FIG_DIR + "correlation_matrix.png",
        RESULT_DIR + "regression_summary.txt"

rule merge_clean:
    input:
        RAW_DIR + "sp500_raw.csv",
        RAW_DIR + "gdp_raw.csv",
        RAW_DIR + "cpi_raw.csv",
        RAW_DIR + "unemployment_raw.csv",
        RAW_DIR + "indpro_raw.csv",
        RAW_DIR + "retail_raw.csv",
    output:
        CLEAN_DIR + "merged_clean.csv"
    shell:
        """
        python scripts/clean_merge.py
        """

rule correlation_matrix:
    input:
        CLEAN_DIR + "merged_clean.csv"
    output:
        FIG_DIR + "correlation_matrix.png"
    shell:
        """
        python scripts/make_correlation_plot.py
        """

rule regression_analysis:
    input:
        CLEAN_DIR + "merged_clean.csv"
    output:
        RESULT_DIR + "regression_summary.txt"
    shell:
        """
        python scripts/run_regression.py
        """

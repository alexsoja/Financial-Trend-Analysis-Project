import pandas as pd
import sys

RAW_FILES = {
    "sp500": "data/raw/sp500_raw.csv",
    "gdp": "data/raw/gdp_raw.csv",
    "cpi": "data/raw/cpi_raw.csv",
    "unemp": "data/raw/unemployment_raw.csv",
    "indpro": "data/raw/indpro_raw.csv",
    "retail": "data/raw/retail_raw.csv",
}

OUTPUT_FILE = "data/clean/merged_clean.csv"


def load_and_clean(filepath, label):
    """
    Load raw CSV file, standardize column names, detect date column,
    rename value column, and prefix columns.
    """

    df = pd.read_csv(filepath)

    # Lowercase all columns
    df.columns = df.columns.str.lower()

    # Fix common FRED pattern: DATE + VALUE (value stored as unnamed column)
    if "unnamed: 1" in df.columns:
        df = df.rename(columns={"unnamed: 1": "value"})

    # Detect date column
    for col in ["date", "observation_date", "timestamp"]:
        if col in df.columns:
            date_col = col
            break
    else:
        print(f"❌ ERROR: No date column found in {filepath}")
        print("Columns:", df.columns.tolist())
        sys.exit(1)

    # Convert date
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col]).rename(columns={date_col: "date"})

    # Add prefix except date
    df = df.add_prefix(f"{label}_")
    df = df.rename(columns={f"{label}_date": "date"})

    return df


def main():
    print("🔧 Cleaning & merging datasets...")

    cleaned_frames = []

    for label, path in RAW_FILES.items():
        print(f"• Processing {label.upper()} from {path}")
        cleaned = load_and_clean(path, label)
        cleaned_frames.append(cleaned)

    # Merge all datasets
    merged = cleaned_frames[0]
    for df in cleaned_frames[1:]:
        merged = pd.merge(merged, df, on="date", how="inner")

    print("\n====== MERGED COLUMNS ======")
    print(merged.columns.tolist())
    print("============================\n")

    print("📈 Creating derived variables...")

    merged = merged.sort_values("date").reset_index(drop=True)

    # Derived variables
    merged["sp500_return"] = merged["sp500_close"].pct_change()
    merged["gdp_growth"] = merged["gdp_value"].pct_change()
    merged["cpi_inflation"] = merged["cpi_value"].pct_change()
    merged["unemp_change"] = merged["unemp_value"].diff()
    merged["indpro_growth"] = merged["indpro_value"].pct_change()
    merged["retail_growth"] = merged["retail_value"].pct_change()

    # Drop NA caused by pct_change
    merged = merged.dropna().reset_index(drop=True)

    merged.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Saved merged dataset to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

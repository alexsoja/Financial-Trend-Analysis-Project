# 🧠 Integrating Stock Market and Economic Indicators for Financial Trend Analysis  
**Final Project — Data Management & Curation (IS 305 / IS 507)**  

---

## 👥 Contributors  
- **Alexander Soja** (University of Illinois Urbana-Champaign, iSchool)  

---

# 📘 Summary  

Understanding how financial markets interact with macroeconomic conditions is a long-standing question in economics and data analytics. This project investigates the relationship between S&P 500 performance and several major U.S. economic indicators over the period 2015–2024, including GDP, CPI inflation, unemployment, industrial production, and retail sales. The purpose of the project is not only to explore these relationships statistically but also to design a fully reproducible data workflow that demonstrates best practices in data curation, cleaning, modeling, and documentation.

Our central research questions are:  
1. **How closely do stock market returns co-move with economic changes on a monthly basis?**  
2. **Do economic indicators help explain or predict equity market movements?**  
3. **Are these relationships consistent across stable and recessionary conditions?**

To answer these questions, we implemented an automated ETL and analysis pipeline using Python and Snakemake. Raw datasets were retrieved from two separate API sources—Yahoo Finance for S&P 500 data and the Federal Reserve Economic Data (FRED) API for macroeconomic indicators. These sources differ in schemas, formats, and sampling frequency, so significant cleaning and standardization were needed. For example, FRED datasets often include unnamed columns requiring renaming, and GDP data—reported quarterly—needed to be forward-filled to align with monthly datasets. We harmonized all sources into a single monthly time-series structure and created derived variables such as returns, percentage growth rates, and unemployment changes.

The final merged dataset captures both normal economic periods and the highly volatile COVID-19 recession. Descriptive analysis highlights that unemployment rose sharply in early 2020, while industrial production and retail activity fell dramatically. The S&P 500 experienced extreme volatility as markets reacted swiftly to uncertainty. These patterns allowed us to observe how market–macro relationships differ between stable and crisis periods.

Correlation analysis revealed that macroeconomic indicators exhibit moderate internal relationships (e.g., industrial production and retail sales co-move strongly), while correlations with stock returns were generally weak. However, isolating the COVID-19 recession period showed dramatically stronger relationships—especially between unemployment and market returns—demonstrating that financial–macro relationships are nonlinear and context-dependent.

OLS regression showed that macro indicators explain only ~9 percent of monthly S&P 500 variation. Retail sales growth was the only statistically significant predictor, while unemployment change was marginal. These results align with financial theory: markets price in expectations ahead of official releases, limiting the predictive power of macro data at monthly frequencies.

All cleaning, merging, analysis, and visualization tasks are automated using Snakemake. Running a single command reproduces the entire workflow, ensuring transparency, reproducibility, and ease of grading.

Overall, this project integrates diverse datasets, applies rigorous data-cleaning practices, and produces meaningful statistical insights about how financial markets respond to economic signals. The workflow demonstrates strong data engineering and curation practices while delivering an analytically grounded narrative.

---

# 🧾 Data Profile  

This project integrates six datasets from two major sources: Yahoo Finance and the Federal Reserve Economic Data (FRED) API. Each dataset required harmonization due to differing formats, frequencies, and metadata quality.

### **S&P 500 Index (Yahoo Finance)**  
Includes daily open, high, low, close, and volume data. Resampled to monthly frequency using end-of-month closing values and monthly aggregations. Data is clean and does not contain personal or sensitive information.

### **GDP (FRED: GDPC1)**  
Real GDP data is provided quarterly. FRED datasets often include unnamed numeric columns; these were renamed programmatically. GDP values were forward-filled to a monthly frequency. Use is permitted under FRED’s open data license.

### **CPI Inflation (FRED: CPIAUCSL)**  
Monthly consumer price index values used to measure inflation. Clean and well-structured. Used to compute month-to-month inflation rates.

### **Unemployment Rate (FRED: UNRATE)**  
Monthly labor force unemployment percentages. Required renaming of generic “Unnamed” columns and type conversion. Contains no personal data.

### **Industrial Production Index (FRED: INDPRO)**  
Measures real output for manufacturing, mining, and utilities. Contains occasional missing placeholders which were cleaned.

### **Retail Sales (FRED: RSAFS)**  
Monthly retail sales totals, representing consumer demand and economic sentiment. Used to compute monthly retail growth rates.

### **Ethical & Legal Constraints**  
All data originates from public, non-personal sources. No consent or privacy concerns exist. FRED explicitly allows redistribution for educational use; Yahoo Finance allows academic research access.

---

# 📄 Data Dictionary  

The final merged dataset (`merged_clean.csv`) contains the following fields:

| Column Name        | Source Dataset | Type     | Description |
|--------------------|----------------|----------|-------------|
| `date`             | All            | datetime | Standardized monthly timestamp used for joining datasets. |
| **S&P 500 Fields** ||||
| `sp500_close`      | Yahoo Finance  | float    | End-of-month closing price. |
| `sp500_high`       | Yahoo Finance  | float    | Highest price during the month. |
| `sp500_low`        | Yahoo Finance  | float    | Lowest price during the month. |
| `sp500_open`       | Yahoo Finance  | float    | Opening price for the first trading day of the month. |
| `sp500_volume`     | Yahoo Finance  | float    | Monthly aggregated trading volume. |
| **GDP** ||||
| `gdp_value`        | FRED (GDPC1)   | float    | Real GDP level (forward-filled). |
| **CPI** ||||
| `cpi_value`        | FRED (CPIAUCSL)| float    | Consumer Price Index value. |
| **Unemployment** ||||
| `unemp_value`      | FRED (UNRATE)  | float    | Unemployment rate (%). |
| **Industrial Production** ||||
| `indpro_value`     | FRED (INDPRO)  | float    | Industrial production index. |
| **Retail Sales** ||||
| `retail_value`     | FRED (RSAFS)   | float    | Retail sales volume. |
| **Derived Variables** ||||
| `sp500_return`     | Derived        | float    | Monthly percent return of S&P 500. |
| `gdp_growth`       | Derived        | float    | Monthly GDP growth. |
| `cpi_inflation`    | Derived        | float    | Month-to-month CPI inflation. |
| `unemp_change`     | Derived        | float    | Change in unemployment rate. |
| `indpro_growth`    | Derived        | float    | Monthly industrial production growth. |
| `retail_growth`    | Derived        | float    | Monthly retail sales growth. |

---

# 🔍 Data Quality Assessment  

A thorough data quality analysis was conducted across completeness, consistency, validity, granularity, and accuracy.

### **Completeness**  
Minimal missingness existed in the raw data. FRED datasets contained occasional placeholders (“.”) which were removed automatically. After merging, all months include complete values for every indicator.

### **Consistency**  
Substantial inconsistency existed in column names, including “Unnamed” fields. All datasets were standardized to use a unified `date` column. Numeric types were converted to floats with invalid entries coerced to NaN.

### **Validity**  
All indicators fall within expected domain ranges (e.g., unemployment 3–15%). S&P 500 historical trends match well-known events like the 2020 crash. Outliers corresponded to real-world events, not errors.

### **Granularity**  
Daily S&P 500 data and monthly/quarterly macroeconomic data required reconciliation. Everything was harmonized to monthly granularity.

### **Accuracy**  
Validated through spot checks against known historical values, financial news, and macroeconomic archives.

**Conclusion:**  
Data quality is high and suitable for statistical analysis.

---

# 📈 Findings  

The dataset provides insight into financial and macroeconomic behavior from 2015–2024. S&P 500 returns averaged ~1% per month but were highly volatile during early 2020. Macro variables followed predictable trends, with sharp disruptions during the COVID-19 recession.

Correlation results show generally weak relationships between S&P 500 returns and macro indicators. Retail sales and industrial production correlate strongly with each other, reflecting consumer–business cycle linkages.

OLS regression explained only ~9% of stock return variation. Retail sales growth was the only significant predictor. Unemployment changes approached significance.

Lagged macroeconomic indicators exhibited even weaker predictive power, supporting semi-strong market efficiency.

A deeper look at the recession period showed dramatically stronger relationships, especially between unemployment and returns. This suggests that macroeconomic conditions influence markets more heavily during periods of economic stress.

Overall, macro data provides context rather than prediction for stock market behavior.

---

# 🔮 Future Work  

There are many directions in which this project could be extended, both analytically and in its data engineering infrastructure. One major limitation of the current work is the relatively small number of monthly observations available between 2015 and 2024. While this period includes both stable and volatile economic regimes, including the COVID-19 recession, the limited sample size constrains the statistical power of regression models and reduces the ability to detect subtle relationships between macroeconomic indicators and market movements. As more data becomes available over time, extending the dataset to span multiple decades would greatly strengthen the analysis. Longer time horizons capture multiple economic cycles, structural shifts, and varied market conditions, allowing for more stable and generalizable findings. A future version of this project could automate incremental updates so that new months of data are seamlessly integrated into the analysis pipeline.

Beyond expanding the temporal coverage, the project could incorporate additional macroeconomic indicators known to influence financial markets. While the current dataset includes GDP, CPI, unemployment, industrial production, and retail sales, future work could integrate high-value predictors such as the yield curve spread, Purchasing Managers’ Index (PMI), federal funds rate targets, commodity prices, or consumer sentiment indices. These series are frequently used in financial modeling and may introduce explanatory signals that the current model is unable to detect. In particular, the yield curve has historically served as a useful predictor of recessions, and integrating it could deepen insights into long-term versus short-term dynamics.

Cross-country macro-financial analysis is another rich area for expansion. Global markets are interconnected, and shocks in one region often propagate to others. Adding international indicators from agencies such as the OECD, Eurostat, or the Bank of Japan would enable analysis of synchronized global cycles, spillover effects, and diversification behavior. This would also allow examination of how U.S. market reactions differ from those in Europe or Asia under similar macroeconomic changes.

From a methodological perspective, the project could be enhanced through the use of nonlinear or machine learning models. While OLS regression provides interpretability and establishes a baseline, it cannot capture nonlinearities or complex interactions between variables. Models such as Random Forests, Gradient Boosting, or neural networks, could uncover hidden patterns and interactions. Even if macroeconomic forecasting remains fundamentally difficult due to market efficiency, these methods could provide insight into variable importance and structural relationships.

On the engineering side, the Snakemake workflow could be expanded to automate raw data acquisition directly from APIs, eliminating the current manual step of placing CSVs into the /data/raw/ directory. Adding validation checks, schema enforcement, and automated alerts for missing or anomalous data would further improve robustness. Integrating unit tests would help ensure long-term maintainability as scripts evolve.

Visualization and communication could also be extended. Developing an interactive dashboard in Streamlit or Plotly Dash would allow users to explore rolling correlations, recession periods, and simulated scenarios dynamically. This would make the project more accessible to non-technical audiences.
Finally, future work could strengthen FAIR principles and archival quality. Publishing the dataset and code in an archival repository such as Zenodo, assigning a DOI, and providing structured metadata (e.g., DataCite or DCAT schemas) would support long-term preservation and reuse. A more extensive README and metadata package could make the project accessible to other researchers, students, or institutions seeking reproducible teaching materials.

---

# 🔁 Reproducibility Instructions  

### **1. Clone the repository**
```bash
git clone https://github.com/alexsoja/Financial-Trend-Analysis-Project
cd Financial-Trend-Analysis-Project
```
### **2. Download data from Box

Raw datasets must be downloaded from Box:
📦 Box Folder: https://uofi.box.com/s/4xmit6ij0q0y0alz2ze2iy651vb5h9nh

Place all downloaded CSV files into:

```bash
data/raw/
```

### **3. Create the Conda environment

```bash
conda env create -f environment.yml
conda activate snakemake-env
```

### **4. Run the full workflow

```bash
snakemake --cores 1
```

This generates:
- data/clean/merged_clean.csv
- figures/correlation_matrix.png
- results/regression_summary.txt

### **5. Expected Folder Structure

```bash
├── data
│   ├── raw
│   └── clean
├── figures
├── notebooks
├── results
├── scripts
├── Snakefile
├── requirements.txt
├── environment.yml
└── README.md
```

# References:

- Yahoo Finance (yfinance)
- Federal Reserve Economic Data (FRED) API
- McKinney, W. (2017). Python for Data Analysis.
- Scikit-learn developers (2011). Machine Learning in Python.
- Snakemake documentation: https://snakemake.readthedocs.io

# License:

This project is released under the MIT License.
All external data follow the licensing requirements of Yahoo Finance and FRED.

# Software Dependencies

Managed via environment.yml and requirements.txt.
Key packages include:
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- yfinance
- fredapi
- snakemake
- scipy
- python-dateutil

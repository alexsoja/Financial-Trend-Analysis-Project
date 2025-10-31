# 📈 Interim Status Report (Milestone 3)
**Project Title:** Integrating Stock Market and Economic Indicators for Financial Trend Analysis  
**Course:** Data Management  
**Date:** October 2025  
**Repository:** https://github.com/alexsoja/Financial-Trend-Analysis-Project
**Team Members:** Alex Soja

---

## 🧭 1. Project Overview
This project analyzes relationships between U.S. stock market performance and key economic indicators using publicly available data from the **Yahoo Finance API** and the **Federal Reserve Economic Data (FRED) API**.  
The goal is to integrate, clean, and analyze data such as the S&P 500 index, GDP, CPI (inflation), unemployment rate, industrial production, and retail sales to identify potential correlations and patterns in financial trends.

All data work has been performed in Jupyter notebooks using the **pandas** library for cleaning, transformation, and merging.  

---

## 🧩 2. Task Updates and Repository Artifacts

| **Task** | **Description** | **Status** | **Artifacts / Files** |
|-----------|-----------------|-------------|------------------------|
| **Data Acquisition** | Retrieved data directly from the FRED API and Yahoo Finance using Python cells in notebooks. Each dataset saved as a CSV in `data/raw/`. | ✅ Completed | - `data_acquisition.ipynb`<br>- `data/raw/*.csv` |
| **Data Cleaning & Preprocessing** | Cleaned datasets to standardize date formats, fix column names, convert data types, and remove null values. | ✅ Completed | - `data_cleaning.ipynb`<br>- `data/clean/*.csv` |
| **Data Integration** | Merged cleaned datasets using pandas on the `date` column to align S&P 500 with multiple economic indicators. | 🟢 Nearly Complete | - `data_cleaning.ipynb`<br>- `data/clean/merged_clean.csv` |
| **Exploratory Data Analysis (EDA)** | Began exploring time series patterns and correlations using plots and summary statistics. |  🔵 Planned | - Placeholder for `notebooks/eda.ipynb` |
| **Documentation & Licensing** | Documented sources, API terms of use, and data attribution. | ✅ Completed | - `ProjectPlan.md` |
| **Automation Setup (Planned)** | Plan to refactor data download and cleaning into a single automated pipeline next milestone. | 🔵 Planned | - Placeholder for `data_pipeline.ipynb` |

---

## 🗓️ 3. Updated Timeline

| **Task** | **Original Target** | **Updated Target** | **Status** |
|-----------|--------------------|--------------------|-------------|
| Data Collection | Week 4 | Week 4 | ✅ Completed |
| Data Cleaning | Week 6 | Week 7 | ✅ Completed |
| Data Integration | Week 7 | Week 8 | 🟢 Nearly Complete |
| EDA & Visualization | Week 9 | Week 10 | 🟡 In Progress |
| Automation / Pipeline | Week 10 | Week 11 | 🔵 Planned |
| Final Report | Week 12 | Week 12 | 🔵 Planned |

---

## 🔄 4. Changes Since Original Project Plan
- **Expanded Scope:** Added new indicators from FRED (CPI, unemployment, industrial production, and retail sales) after realizing GDP alone had limited data points.  
- **No External Scripts:** Originally planned to create `.py` scripts for automation, but for simplicity, all work is currently in **Jupyter notebooks**. Automation will be integrated later.  
- **Simplified Data Integration:** Continued using **pandas merges** instead of SQL or DuckDB for flexibility.  
- **Timeline Adjustment:** Added one week to cleaning and EDA phases due to new indicator integrations.  
- **License Documentation:** Updated `ProjectPlan.md` file with usage terms for FRED and Yahoo Finance APIs.

---

## ⚙️ 5. Current Challenges
- **Data Frequency Mismatch:** FRED indicators are monthly or quarterly, while S&P 500 data is daily. To handle this, the stock data will be resampled to monthly averages for consistent merging.  
- **Small GDP Dataset:** The GDP dataset only includes ~18 rows (quarterly), which limits its analytical usefulness. To address this, we incorporated higher-frequency indicators.  
- **Automation:** Data acquisition and cleaning are currently manual notebook cells; automating these will improve reproducibility in the next milestone.

---

## 🚀 6. Next Steps
1. Complete integration of all economic indicators into a single merged dataset.  
2. Conduct correlation analysis between indicators and market returns.  
3. Create time series visualizations (e.g., rolling averages, scatter plots).  
4. Develop a reproducible pipeline for automatic data retrieval and cleaning.  
5. Prepare final report and dashboard visualizations.

---

## 👥 7. Team Member Contributions

### **Alex Soja**
- Implemented data acquisition scripts for both APIs.  
- Built initial integration workflow 
- Developed cleaning logic and tested with sample CSVs.  
- Drafted this milestone report.
- Conducted exploratory data visualizations.  
- Assisted in documentation and feedback incorporation.
- Worked on refining schema definitions and license documentation.  
- Managed GitHub release and tagging process.

---

## 🏷️ 8. Repository & Release Information
- **GitHub Repo:** https://github.com/alexsoja/Financial-Trend-Analysis-Project  
- **Milestone 3 Tag:** `status-report`  
- **Release Page:**   
- **Commit Summary:** Includes all updated notebooks, scripts, and `StatusReport.md`.


*End of Status Report.*

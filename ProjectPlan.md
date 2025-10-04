# Integrating Stock Market and Economic Indicators for Financial Trend Analysis
## Overview: 
The goal of this project is to analyze the relationship between financial market performance and macroeconomic indicators in the United States. 
By integrating stock market data with economic indicators such as GDP growth, inflation (CPI), and unemployment rates, 
this project explores how economic conditions correlate with or predict market behavior over time. 
The project will demonstrate the full data management lifecycle (from data collection and storage to integration, cleaning, analysis, and documentation)
using Python and SQL for implementation. 

## Research Questions: 
- How do macroeconomic indicators (GDP, CPI, and unemployment rate) correlate with major stock market indices like the S&P 500 over time?
- Can changes in economic indicators help predict stock market trends or volatility?
- What patterns emerge when comparing different time periods (e.g., pre- vs. post-pandemic)?

## Team:
Team Members: Me (Alexander Soja)
Responsibilities:
- Project design and research questions
- Data collection and acquisition
- Data integration and cleaning (Python + SQL)
- Automation & reproducibility setup (ETL pipeline, GitHub, Markdown docs)
- Final report and presentation
  
## Datasets:
This project will use two trustworthy and open datasets with different formats and access methods:

Stock Market Data (via Yahoo Finance / yfinance API):
- Access Method: Python API (no authentication required)
- Content: Historical daily data for the S&P 500 and selected individual stocks (e.g., AAPL, MSFT, GOOGL) including open, close, high, low, and volume.
- Format: Retrieved via JSON and loaded into Pandas DataFrames or SQL tables.
- Source: Yahoo Finance (via open yfinance library)

Macroeconomic Indicators (via FRED API):
- Access Method: REST API (requires free API key)
- Content: Quarterly or monthly data on GDP growth, Consumer Price Index (CPI), and unemployment rate.
- Format: JSON/CSV (depending on request format)
- Source: Federal Reserve Economic Data (FRED)

Integration Strategy:  
Datasets will be joined on time (date) and region (U.S.) to align stock and economic data for correlation analysis.

## Timeline: 
1. Create GitHub repo & ProjectPlan.md	-	(Initial plan & tag release)
2. Collect data from APIs -	(Raw datasets & metadata)
3. Set up SQL schema & load data - (Database setup)
4. Integrate and clean data - (Merged dataset)
5. Automate ETL pipeline - (Python script)
6. Analyze trends & visualize results - (Jupyter notebook)
7. Finalize report & documentation - (Final Markdown report & GitHub release)

## Storage & Organization:
Storage Type: Relational database (SQLite or PostgreSQL)

Schema Design:
- stocks (ticker, date, open, close, volume)
- economic_indicators (indicator_name, date, value)
- merged_data (date, sp500_close, gdp_growth, cpi, unemployment_rate)

Organization:
- /data/ → raw and processed datasets
- /src/ → Python scripts for ETL
- /docs/ → Markdown reports and metadata
- /notebooks/ → Jupyter notebooks for exploration
  
## Constraints: 
- Limited to publicly available financial and economic data
- API rate limits (minor delay when collecting large data spans)
- Only U.S. market/economic indicators due to scope

## Gaps:
- Deciding which specific stock index or company tickers to include
- Determining whether to use monthly or quarterly aggregation
- Considering to include lag correlation analysis (possibly too advanced step)

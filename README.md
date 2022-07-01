# Trader-int 1.0
Twitter Botscore extractor

## Description:
This software extracts Tweets for a list of equity cashtags and assigns bot scores to the users. Results are saved a MySQL database. 

## Markets covered:
ASX (Australian equities) - All tickers
NYSE - Market capitalisation >$10B
AMEX - Market capitalisation >$10B
NASDAQ - Market capitalisation >$10B

## Requirements:
Python3.9 (or above)
MySQL server
Twitter API key
Botometer API key (Rapid API)



### Step 1: 
Input your server settings in database_config.py
Input your API keys in api_keys.py

### Step 2:
For Australian tickers, download the .XLS file from:: https://www2.asx.com.au/content/dam/asx/issuers/ISIN.xls
For US tickers, download the .CSV file from: https://www.nasdaq.com/market-activity/stocks/screener

### Step 3:
Extract cashtags and clean up the ticker list with:
clean-ticker-list.py

### Step 4:
Begin Twitter scraper with:
run-search.py

### Step 5:
Begin Botometer calls with:
get-bot-scores.py

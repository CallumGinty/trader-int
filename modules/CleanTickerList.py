#!/usr/bin/env python
# coding: utf-8
import pandas

autickers = pandas.read_excel("./ISIN.xls")
ustickers = pandas.read_csv("nasdaq_screener_1656649805299.csv")
filename = "tickerlist.csv"

def cleaning(autickers, ustickers):
	print("#### Cleaning ticker list ####")
	print ("Raw AU tickers dataframe shape:", autickers.shape)
	print ("Raw US tickers dataframe shape:", ustickers.shape)
	print("Removing empty rows...")
	autickers.dropna(axis=0, how='any', inplace=True) #drop empty rows. In the AU tickers, these rows are at the top of file. 

	print("Removing non-equity tickers...")
	autickers = autickers[autickers['Security type'] == "ORDINARY FULLY PAID"] #drop rows that arent ordinary fully paid shares

	print("Removing duplidate rows...")
	autickers.drop_duplicates(subset='Company name', keep="first", ignore_index=True) # drop any duplicate ASX code rows

	print("Renaming columns...")
	au = autickers.rename(columns = {'ASX code': 'Symbol'}, inplace=False) # creating new variable here to avoid the SettingWithCopyWarning.
	us = ustickers.rename(columns = {'Name': 'Company name'}, inplace=False) # Could also remove the warning with "df.is_copy = False"
	
	return au, us

def merge_and_export(autickers, ustickers):
	print("Joining tables...")
	combinedtickers = pandas.concat([autickers, ustickers], ignore_index=True) #ignore index, clears and resets the index.
	print ("Combined shape:", combinedtickers.shape)

	print("Creating a list of hashtags...")
	hashtag = [ ("#" + combinedtickers ) for combinedtickers in combinedtickers["Symbol"]]
	combinedtickers['hashtags'] = hashtag

	print("Creating a list of cashtags...")
	cashtag = [ ("$" + combinedtickers ) for combinedtickers in combinedtickers["Symbol"]]
	combinedtickers['cashtags'] = cashtag

	print("Exporting out to a csv file:", filename)
	combinedtickers.to_csv(filename)
	print("Ticker clean and merge complete!\n")


au, us = cleaning(autickers, ustickers)
merge_and_export(au, us)


#!/usr/bin/env python
# coding: utf-8
import pandas

autickers = pandas.read_excel("./ISIN.xls")
ustickers = pandas.read_csv("nasdaq_screener_1656649805299.csv")
print ("AU shape:", autickers.shape)
print ("US shape:", ustickers.shape, "\n")

print("Removing empty rows...")
autickers.dropna(axis=0, how='any', inplace=True) #drop empty rows. In the AU tickers, these rows are at the top of file. 

print("Removing non-equity tickers...")
autickers = autickers[autickers['Security type'] == "ORDINARY FULLY PAID"] #drop rows that arent ordinary fully paid shares

print("Removing duplidate rows...")
autickers.drop_duplicates(subset='Company name', keep="first", ignore_index=True) # drop any duplicate ASX code rows

print("Renaming columns...")
autickers.rename(columns = {'ASX code': 'Symbol'}, inplace=True)
ustickers.rename(columns = {'Name': 'Company name'}, inplace=True)


###############
print ("AU shape:", autickers.shape)
print ("US shape:", ustickers.shape, "\n")
print("Joining tables...")
combinedtickers = pandas.concat([autickers, ustickers], ignore_index=True) #ignore index, clears and resets the index.
print ("Combined shape:", combinedtickers.shape, "\n")

print("Creating a list of hashtags...")
hashtag = [ ("#" + combinedtickers ) for combinedtickers in combinedtickers["Symbol"]]
combinedtickers['hashtags'] = hashtag

print("Creating a list of cashtags...")
cashtag = [ ("$" + combinedtickers ) for combinedtickers in combinedtickers["Symbol"]]
combinedtickers['cashtags'] = cashtag


print("Exporting out to a csv file...")
combinedtickers.to_csv(r'tickerlist.csv')

print("Cleaning complete!")


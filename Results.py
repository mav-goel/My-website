import pandas_datareader as web


DataSource = "yahoo"

def GetStockPrice(Stock, Date1, Date2):
    
    results = web.DataReader(Stock , DataSource, Date1, Date2)["Adj Close"]

    return results[0]





   
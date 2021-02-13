import pandas_datareader as web


DataSource = "yahoo"

def GetStockPrice(Stock, Date1, Date2):
    
    h = web.DataReader(Stock , DataSource, Date1, Date2)["Adj Close"]

    return h[0]


##def divide(a,b):
 #   try:
   #     c = a/b
   #     return c
   # except ZeroDivisionError:
    #    return "You stupid!"

#x = int(input("Num1: "))
##y = int(input("Num2: "))
#z = divide(x,y)
#print(z)





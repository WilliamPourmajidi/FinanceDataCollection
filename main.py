import yfinance as yf
from pandas_datareader import data as pdr

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

data = yf.download("MSFT AAPL IBM", start="2021-01-01", end="2021-12-30")

print(data)





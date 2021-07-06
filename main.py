import pandas as pd

orcl = pd.read_excel("./DATA/ORCL.xlsx", sheet_name="Sheet1")
btc = pd.read_excel("./DATA/BTC-USD.xlsx", sheet_name="Sheet1")
ltc = pd.read_excel("./DATA/LTC-USD.xlsx", sheet_name="Sheet1")
tsla = pd.read_excel("./DATA/TSLA.xlsx", sheet_name="Sheet1")
nflx = pd.read_excel("./DATA/NFL=X.xlsx", sheet_name="Sheet1")

data = pd.DataFrame()


print(data.head(10))

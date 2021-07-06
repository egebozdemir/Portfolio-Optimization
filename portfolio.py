import numpy as np
import pandas as pd
import io


df_port = pd.read_excel("./DATA/united.xlsx", sheet_name="Sayfa1")
df_stocks = pd.read_excel("./DATA/united.xlsx", sheet_name="Sayfa2")


del df_port['Unnamed: 5']
# print(df_port)

# df_port.reset_index(drop=True, inplace=True)
# print(df_port)

# port_return = df_port.iloc[0][0]
# print(port_return)


df_stocks.reset_index(drop=True, inplace=False)
df_stocks.set_index(df_stocks.iloc[1])
# print(df_stocks.head(10))
# print(df_stocks.iloc[0][2])
print(df_stocks.index)

import pandas as pd

data = []

with open("AMBA.csv", "r") as file:
    for line in file.readlines():
        row = line.replace("\n", "").split(",")
        data.append(row)

df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df[1:]
df = df.set_index("Date")

df.to_excel(excel_writer="./AMBA.xlsx")

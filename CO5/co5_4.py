import pandas as pd
df=pd.read_csv("Financial Sample.csv")
print(df)
print(df.head())
print(df.tail())
print(df[["Segment","Country"]].head())

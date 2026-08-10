import polars as pl
df = pl.read_csv(r"C:\Users\LENOVO\Desktop\Data Analitika\d\NYC Accidents 2020.csv")
print(df.head(30))
#df.null_count()

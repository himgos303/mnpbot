import pandas as pd

df = pd.read_csv('6xxx-in-mob-prefix.csv')
print("Columns in CSV:", df.columns.tolist())
print(df.head())

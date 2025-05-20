# save this as merge_prefix_data.py
import pandas as pd
import glob

# get all matching CSVs
files = glob.glob("*xxx-in-mob-prefix.csv")

# merge all into one DataFrame
df_list = [pd.read_csv(f) for f in files]
merged_df = pd.concat(df_list, ignore_index=True)

# save it as prefix_database.csv
merged_df.to_csv("prefix_database.csv", index=False)
print("Merged into prefix_database.csv with", len(merged_df), "rows.")

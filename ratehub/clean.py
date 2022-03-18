import pandas as pd


def trim_all_columns(df):
    """
    Trim whitespace from ends of each value across all series in dataframe
    """
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)


df = pd.read_csv("output.csv")  # Read the csv file
df = df.dropna()  # Drop any na rows
df = df.drop_duplicates()  # Drop any duplicates
df = trim_all_columns(df)  # Trim the columns from whitespaces
df = df.sort_values(by="rate")  # Sort it by rate
df = df[0:5]  # Only get the top 5 rates
df = df.reset_index(drop=True)  # Reset index

df.to_csv("output.csv")  # Output to csv
print(df)  # Print dataframe

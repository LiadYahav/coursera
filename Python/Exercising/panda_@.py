import pandas as pd
file_name = 'TopSellingAlbums.csv'
df = pd.read_csv(file_name)
file2_name = 'TopSellingAlbums.xlsx'
df2 = pd.read_excel(file2_name)
print(df.loc[1, "Album"])


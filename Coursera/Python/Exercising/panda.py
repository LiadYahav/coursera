import pandas
import pandas as pd
#Define a dictionary 'x'

x = {'Name': ['David', 'Samuel', 'Terry', 'Evan'],
     'Age': [27, 24, 22, 32],
     'Country': ['UK', 'Canada', 'China', 'USA'],
     'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
     'Marks': [85, 72, 89, 76]}

df = pandas.DataFrame(x)
df2 = df
df2 = df2.set_index("Name")

# print(df.iloc[0:2, 0:3])
# print(df.loc[0:1, 'Age':'Marks'])
# print(df2.loc['Samuel':'Evan', 'Age':'Country'])
print(df.loc[2:3, "Name":"Country"])

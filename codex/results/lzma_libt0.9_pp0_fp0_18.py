import lzma
lzma.open(os.path.join(pwd, 'data', 'w5_data.lzma'), mode="r").read()

df = pd.read_csv(os.path.join(pwd, 'data', 'w5_data.csv'), index_col=0)

# use first column as index
df.columns = df.iloc[0]

# remove first row
df = df.iloc[1:-1]
 
df.head()

# getting a year columns
df_2005 = df.filter(regex=("2005"), axis=1)
df_2018 = df.filter(regex=("2018"), axis=1)

# getting a country column
country_column = df.filter(regex=("2005"), axis=0).iloc[:, 0]

# change index
df_2005 = df_2005.set_index(country_column)
df_2018 = df_2018.set_index(country_column)

# add columns that are changed
change = pd.Series(dtype='float64', name='

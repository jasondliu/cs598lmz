import bz2
bz2.BZ2File(path)

# Read the file into a DataFrame: df
df = pd.read_csv(path)

# Print the head of df
print(df.head())

# Check the shape: df_shape
df_shape = df.shape

# Print the shape of df
print(df_shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())

# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())

# Read in the file: df1
df1 = pd.read_csv(data_file)

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv(data_file, header=0, names

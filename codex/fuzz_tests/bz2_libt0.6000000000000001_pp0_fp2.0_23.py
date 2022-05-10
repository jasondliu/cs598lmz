import bz2
bz2_file = bz2.BZ2File('./data/sample_data.csv.bz2')
data = bz2_file.read()

# Save data to file
with open('./data/sample_data_from_bz2.csv', 'wb') as f:
    f.write(data)

# Load data
df = pd.read_csv('./data/sample_data_from_bz2.csv')
df.head()

# Only keep numerical data
df = df._get_numeric_data()
df.head()

# Plot data
df.plot(kind='scatter', x='col_0', y='col_1')
plt.show()

# Compare with original data
df_original = pd.read_csv('./data/sample_data.csv')
df_original.head()

# Only keep numerical data
df_original = df_original._get_numeric_data()
df_original.head()

# Plot data
df_original.plot(kind='scatter', x

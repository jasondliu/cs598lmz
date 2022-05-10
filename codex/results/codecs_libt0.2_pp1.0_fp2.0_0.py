import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
# Read in the data

# Read in the data
data = pd.read_csv('../data/raw/data.csv')

#%%
# Clean the data

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data.dropna()

# Remove the rows with missing values
data = data

import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Load the data
data = pd.read_csv('data/data.csv', encoding='utf-8')

# Remove the first column
data = data.iloc[:, 1:]

# Remove the first row
data = data.iloc[1:, :]

# Remove the last column
data = data.iloc[:, :-1]

# Remove the last row
data = data.iloc[:-1, :]

# Remove the first column
data = data.iloc[:, 1:]

# Remove the first row
data = data.iloc[1:, :]

# Remove the last column
data = data.iloc[:, :-1]

# Remove the last row
data = data.iloc[:-1, :]

# Remove the first column
data = data.iloc[:, 1:]

# Remove the first row
data = data.iloc[1:, :]

# Remove the last column
data = data.iloc[:, :-1]

# Remove the last

import bz2
bz2.BZ2File('data/train.csv.bz2')

# Importing the data
import pandas as pd
data = pd.read_csv('data/train.csv.bz2', compression='bz2')

# Print the head of the data
print(data.head())

# Print the shape of the data
print(data.shape)

# Print summary statistics of the data
print(data.describe())

# Importing the data
import pandas as pd
data = pd.read_csv('data/train.csv.bz2', compression='bz2', nrows=5)

# Print the head of the data
print(data.head())

# Print the shape of the data
print(data.shape)

# Importing the data
import pandas as pd
data = pd.read_csv('data/train.csv.bz2', compression='bz2', nrows=5, chunksize=10)

# Print the shape of the first chunk
print(next(data).shape)

# Import

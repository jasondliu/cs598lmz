from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File('aviation.csv.bz2', 'r'))

# Read in the data
aviation_data = pd.read_csv('aviation.csv.bz2', sep=',', compression='bz2')

aviation_data.head()

# How many rows and columns are in the dataset?

rows = aviation_data.shape[0]
columns = aviation_data.shape[1]

print(rows)
print(columns)


# What are the names and data types of the columns?

aviation_data.dtypes

# How many incidents are recorded in this dataset?

incidents = aviation_data['Event Id'].nunique()

print(incidents)

# What are the top 10 causes of aviation incidents in the dataset?

aviation_data['Investigation Type'].value_counts().nlargest(10)

# How many types of aircraft models are recorded in the dataset?

aviation_data['Aircraft Category'].nunique()

# How many types

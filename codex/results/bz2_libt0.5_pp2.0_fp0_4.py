import bz2
bz2_file = bz2.BZ2File(file_name)
data = bz2_file.read()
bz2_file.close()

# Decompress the data
data = zlib.decompress(data)

# Write the data to a file
new_file = open(file_name[:-4], 'wb')
new_file.write(data)
new_file.close()

# Read the raw file as a pandas dataframe
df = pd.read_csv(file_name[:-4], header=None, names=['CICIDS2017'])

# Write to csv
df.to_csv('../../data/raw/CICIDS2017.csv', index=False)

# Delete the uncompressed file
os.remove(file_name[:-4])

# Print out the shape of the dataframe
print(df.shape)

# Display the first 5 rows of the dataframe
df.head()

# Load the labels
labels = pd.read_csv('../../data/raw/CICIDS2017_

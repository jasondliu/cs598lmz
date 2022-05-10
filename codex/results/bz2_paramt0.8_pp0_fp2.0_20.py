from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../geodata/us_zipcodes.csv.bz2').read())

filename = '../geodata/us_zipcodes.csv.bz2'

with open(filename, 'rb') as f:
    data = BZ2Decompressor().decompress(f.read())
    
# list of strings
data = data.decode().split('\n')

# list of lists
data = [row.split(',') for row in data]

#convert to a dataframe
us_zipcodes_df = pd.DataFrame(data[1:], columns=data[0])

us_zipcodes_df.head()

# look at the columns
us_zipcodes_df.columns
# convert zip code to string
us_zipcodes_df['zip'] = us_zipcodes_df.zip.astype(str)

# look at the data type
us_zipcodes_df.dtypes

# note - lat and long are not in correct data types
# need to convert
us_zipcodes_

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.read())

# bz2.read() returns bytes, so we need to decode it to a string
# the string is encoded in utf-8
# the string is not a valid json, so we need to remove the first and last characters

import json
json.loads(bz2.read().decode('utf-8')[1:-1])

# the json is a list of dictionaries
# we can convert it to a dataframe

import pandas as pd
df = pd.DataFrame(json.loads(bz2.read().decode('utf-8')[1:-1]))
df.head()

# we can use the pandas to_csv method to write the dataframe to a csv file
# the index=False argument will prevent pandas from writing the index to the csv

df.to_csv('data.csv', index=False)

# we can read the csv file into a dataframe
# the read_csv method will automatically convert the columns to the appropriate types

df = pd.read_csv('data

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(zipped_file)

# write file to the destination
with open('/home/kiran/test_test.csv', 'wb') as f:
    f.write(zipped_file)
    f.close()
df = pd.read_csv('/home/kiran/test_test.csv')
df.head()

# get all columns as list
cols = list(df.columns)

# remove the special chars from all the columns
for col in cols:
    df.rename(columns=lambda x: x.replace('.', ''), inplace=True)

# assign to the variable
cols = list(df.columns)

# drop all the special chars from the cols list
for col in cols:
    cols[cols.index(col)] = col.replace('.', '')

# replace all spaces with _
cols = [col.replace(' ', '_') for col in cols]

# replace all _nan with nan
cols = [col.replace('_nan',

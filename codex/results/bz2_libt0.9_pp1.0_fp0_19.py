import bz2
bz2.BZ2File(bz2_filename)

#get the bzip file
bz2_file = bz2.BZ2File(bz2_filename)
bz2_file.readlines()

#get the uncompressed file
bz2_uncompressed_data = bz2.decompress(bz2_file.read())

#store the uncompressed data
uncompressed_filename = home + '/Desktop/free-zipcodes-geocodes.csv'
open(uncompressed_filename, 'wb').write(bz2_uncompressed_data)

print 'Completed decompression.\n\n'

#get zipcode dataset
df_zipcodes = pd.read_csv(uncompressed_filename)
df_zipcodes['zipcode'] = df_zipcodes['zipcode'].str[:5]
df_zipcodes['zipcode'] = df_zipcodes['zipcode'].astype(int)
df_zipcodes['latitude'] = df_zipcodes['latitude'].astype(float)
df

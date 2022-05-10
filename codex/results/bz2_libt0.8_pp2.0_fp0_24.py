import bz2
bz2.open('C:\\Users\\Alejandro\\Documents\\motivation.txt.bz2', 'rb')

# Read sample data
f = bz2.open('C:\\Users\\Alejandro\\Documents\\motivation.txt.bz2', 'rb')
dataset = f.read()
f.close()

# Decompress data
decompressed_data = bz2.decompress(dataset)

# Print first 1000 characters in the decompressed data
print("The first 1000 characters in the decompressed data are\n{}".format(decompressed_data[0:1000]))

# Write compressed data to file
data_to_compress = 'This is the data to compress'

with bz2.open('C:\\Users\\Alejandro\\Documents\\data_file.bz2', 'wb') as newfile:
  newfile.write(data_to_compress.encode('utf-8'))

# Read the compressed data from file
with bz2.open('C:\\Users\\Alejandro\\Documents\\data_file

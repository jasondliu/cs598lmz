import bz2
# Test BZ2Decompressor

decompress = bz2.BZ2Decompressor()

de_data = decompress.decompress(compressed_data)
print(de_data)

if de_data == original_data:
    print("The original and decompressed data are the same.")
else:
    print("The original and decompressed data are different.")

# Make sure to close the decompression object
decompress.close()
 
# Write to a file

data_file = open("test.txt", "wb")
data_file.write(compressed_data)
data_file.close()

# This can now be read in the usual way

read_data = bz2.BZ2File("test.txt", "rb").read()
print(read_data)

# If a file is already compressed and is being read in a piece at a time,
# the BZ2File object can create a decompression object for each read

data_file = open("test.txt", "wb")
data_file.write(compressed_data)
data_file.close

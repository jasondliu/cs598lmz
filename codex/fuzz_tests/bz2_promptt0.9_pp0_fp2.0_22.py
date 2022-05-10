import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
# Create empty bytearray to store decompressed data
uncompressed_data = bytearray()
f = open('sample_small.csv.bz2', 'rb')
# Read first 4 bytes of BZ2 file to determine blocksize
file_size_bytes = f.read(4)
print("File size in bytes:", int.from_bytes(file_size_bytes, byteorder='big'))

for chunk in iter(lambda: f.read(100 * 1024), b''):
    uncompressed_data += d.decompress(chunk)
    
# Decompress remainder
uncompressed_data += d.decompress(d.flush())
f.close()
print("Uncompressed size in bytes:", len(uncompressed_data))
# Write decompressed data to a file
b = open("sample_small.csv", "wb")
b.write(uncompressed_data)
b.close()

# Now read CSV into a dataframe. We can check the data is valid by checking

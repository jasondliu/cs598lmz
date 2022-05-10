import bz2
# Test BZ2Decompressor

# In a loop, decompress data from a file-like object
data = bz2.BZ2File(path, 'rb')
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda : data.read(100 * decompressor.decompress(data.read(100))), b''):
    process(chunk)
    
# Use the decompress() method to decompress a
# compressed string
uncompressed_data = decompressor.decompress(compressed_data)

# After calling decompress(), the decompressor
# object can no longer be used; any attempt to
# call decompress() will fail
uncompressed_data = bz2.decompress(compressed_data)

# Compression objects
with bz2.BZ2File('file.bz2', 'wb') as output:
    with open('file', 'rb') as input:
        output.writelines(input)
import gzip
# Test GzipFile

# Use the compress() function to compress a
# string of data
compressed_

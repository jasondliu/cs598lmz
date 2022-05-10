import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
print(len(decompressed_data))

print(decompressed_data == original_data)

print(decompressor.unused_data)

print(data == original_data)
# Test the BZ2File class
filename = '/tmp/bzipped-text.bz2'
with open(filename, 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File(filename, 'rb') as f:
    decompressed_data = f.read()

print(decompressed_data == original_data)

# bz2.BZ2File is a context manager
import re
pat = re.compile(rb'\w+')
with open('/tmp/lorem.txt', 'rb') as input:
    with bz2.BZ2File('/tmp/lorem.bz2', 'wb') as output:
       

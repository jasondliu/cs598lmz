import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
decompressed_data = d.decompress(compressed_data)

# You can check that the decompressed data is equal to the original data
assert(decompressed_data == original_data)
 
# There is also a BZ2File class like the GzipFile class
# that works with files
# with bz2.BZ2File('file.bz2', 'w') as f:
# f.write(original_data)

# Read the compressed data in file.bz2
# with bz2.BZ2File('file.bz2', 'r') as f:
# compressed_data = f.read()
 
# You can check that the decompressed data is equal to the original data
# assert(d.decompress(compressed_data) == original_data)
 
# Show the decompressed data
# decompressed_data

import sys, string
print(sys.getsizeof("123456789abcdefgh"))


print("abraka dabra".upper())

from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

print(decompressed)

# Using the hashlib module
import hashlib, binascii

hash_algorithm = "sha1"
filename = "python-3.7.2.dll"

with open(filename, "rb") as f:
    file_contents = f.read()
    hasher = getattr(hashlib, hash_algorithm)
    hash_value = hasher(file_contents).hexdigest()
    
    print("The hex string for the file is: {}.".format(hash_value))
    
# The hex string for the file is: 89862bae2785d37aad3c12e349ab2638762ddcae.

hash_value = binascii.hexlify(file_contents).decode()
print(hash_value[0:8])
# b'89a05a34'

# Hash Algorithms
# ----------------------
# To get a list of available algorithms, use the algorithm_name() method in the hashlib module.

import

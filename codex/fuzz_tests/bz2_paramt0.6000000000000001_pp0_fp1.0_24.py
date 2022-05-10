from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bytes(bz_data))

# Convert from bytes to string
decoded_data = decoded_data.decode("utf-8")

# In Python 3, the decompressed data will be a "bytes" object.
# If you have a newer version of the "bz2" module, you can supply
#   the parameter "auto_decode=True" which will automatically turn
#   the "bytes" data into a string.
# In either case, you can convert the value of "data" into a string
#   with a str() cast or by using the .decode() method.
print(type(decoded_data))
decoded_data = str(decoded_data)
print(type(decoded_data))

# Split the data into links
links = decoded_data.split()

print(len(links))

# Print the first two links
print(links[:2])

# <script.py> output:
#     <class 'bytes'>
#     <class 'str'>
#     2286
#     ['http://www.

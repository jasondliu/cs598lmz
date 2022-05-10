from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Compress the string
# bz2.compress(bytes(string, 'utf-8'))

# Decompress the string
# bz2.decompress(bytes(compressed_string, 'utf-8'))

# Print the result
# print(decompressed_string)

# Assign the compressed string to compressed_string
compressed_string = bz2.compress(bytes(string, 'utf-8'))

# Print the length of the compressed string
print(len(compressed_string))

# Decompress the compressed string
decompressed_string = bz2.decompress(compressed_string)

# Print the length of the decompressed string
print

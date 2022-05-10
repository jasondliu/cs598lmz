import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Read the first 5 bytes of the compressed file
with open('example.bz2', 'rb') as input:
    next_5_bytes = input.read(5)

# Decompress the first 5 bytes
decompressed_data = decompressor.decompress(next_5_bytes)

# Print the first 5 bytes of the decompressed file
print(decompressed_data)

# Print the entire decompressed file
print(decompressor.decompress(input.read()))

# Decompress the entire file using bz2.decompress()
print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# Print the first 5 bytes of

import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(compressed_data)
result == original_data

# Test BZ2File
with bz2.BZ2File('spam.bz2', 'wb') as output:
    output.write(original_data)

with bz2.BZ2File('spam.bz2', 'rb') as input:
    print(input.read(100))

print(len(result), len(original_data))

# Test bz2.compress
compressed = bz2.compress(original_data)
print(len(compressed))

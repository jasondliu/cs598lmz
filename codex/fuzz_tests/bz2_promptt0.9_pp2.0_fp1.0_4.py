import bz2
# Test BZ2Decompressor to decompress method
bz2_decompressor = bz2.BZ2Decompressor()
original_content = bz2_decompressor.decompress(compressed_data)
print(len(original_content))
print(len(CATEGORIES_HTML))
print(original_content)

# Compare the decompressed HTML string with the original HTML string
for i, (byte1, byte2) in enumerate(zip(original_content, CATEGORIES_HTML)):
    if byte1 != byte2:
        print('Difference 

import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(bz_data))

text = 'This is the original text.'
print('Original: ', text)
compressed = bz2.compress(text.encode('utf-8'))
print(compressed)
print('Decompressed: ', bz2.decompress(compressed))

PYTHONIOENCODING = 1
print('Decompressed: ', decompressor.decompress(compressed).decode())

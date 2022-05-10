import bz2
# Test BZ2Decompressor.decompress()
decomp = bz2.BZ2Decompressor()
original = b'This is the original text.'
compressed = decomp.compress(original) + decomp.flush()
print('Original:', original)
print('Compressed:', compressed)
decompressed = decomp.decompress(compressed)
print('Decompressed:', decompressed)

print(decomp.unused_data)

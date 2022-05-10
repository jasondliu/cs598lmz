import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
result = decomp.decompress(compressed_data)
print(result)

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
result = comp.compress(test_string) + comp.flush()
print(result)

# Test BZ2File
with bz2.BZ2File(filename, 'w') as f:
    f.write(test_string)

with bz2.BZ2File(filename, 'r') as f:
    print(f.read())

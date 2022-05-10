import bz2
# Test BZ2Decompressor

data = open("sample.bz2", "rb").read()

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
result += decompressor.flush()

print(result)

print("-" * 80)

# Test BZ2File

bz_file = bz2.BZ2File("sample.bz2")
result = bz_file.read()
print(result)

print("-" * 80)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
result = compressor.compress(b"this is a test")
result += compressor.flush()

print(result)

print("-" * 80)

# Test BZ2File (compress)

bz_file = bz2.BZ2File("compressed_file.bz2", "w")
bz_file.write(b"this is a test")
bz_file.close()

print(open("compressed_file.b

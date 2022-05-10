import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress("BZh91AY&SY")
print(result)

result += decompressor.decompress("AoP4")
result += decompressor.flush()
print(result)

# Compress data
data = b"Lots of data here"
bz2.compress(data)

# Using the compressed stream with BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Using the compressed stream with BZ2File
with open("somefile.bz2", "wb") as f:
    with bz2.BZ2File(f, "w") as compressor:
        for line in data:
            compressor.write(line)


# Using the compressed stream with BZ2File
with open("somefile.bz2", "rb") as f:
    with bz2.BZ2File(f) as decompressor:
        for line in decompressor:


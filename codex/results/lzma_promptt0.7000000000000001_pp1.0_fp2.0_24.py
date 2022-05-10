import lzma
# Test LZMADecompressor & LZMACompressor

# decompress
lzc = lzma.LZMADecompressor()
result = lzc.decompress(testLZMA)
print(result)

# compress
lzc = lzma.LZMACompressor()
result = lzc.compress(testLZMA)
print(result)


# result = lzc.flush()
# print(result)

# lzc.returncode

# lzc.unused_data

# lzc.decompress(testLZMA)

# lzc.reset()

# lzc.decompress(testLZMA)

# lzc.reset()

# lzc.decompress(testLZMA)

# lzc.returncode

# lzc.decompress(testLZMA)

 
# lzc.eof

# lzc.eof

# lzc.decompress(testLZMA)

# lz

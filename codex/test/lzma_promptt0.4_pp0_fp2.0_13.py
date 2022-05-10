import lzma
# Test LZMADecompressor

f = open('test.lzma', 'rb')
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(f.read())
print(data)

# Test LZMACompressor

compressor = lzma.LZMACompressor()
data2 = compressor.compress(data)
print(data2)

data3 = compressor.flush()
print(data3)

# Test LZMAFile

f2 = lzma.LZMAFile(f)

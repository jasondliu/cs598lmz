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
print(f2.read())

f3 = lzma.LZMAFile('test.lzma', 'w')
f3.write(data)
f3.close()

f4 = lzma.LZMAFile('test.lzma', 'r')
print(f4.read())

f5 = lzma.LZMAFile('test.lzma', 'a')
f5.write(data)
f5.close()

f6 = lzma.LZMA

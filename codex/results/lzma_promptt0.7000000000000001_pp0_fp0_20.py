import lzma
# Test LZMADecompressor's internal buffer by decompressing a large chunk of data
# at once.
data = b'A' * 2**20
comp = lzma.LZMACompressor()
data1 = comp.compress(data)
data2 = comp.compress(data)
data3 = comp.flush()
dec = lzma.LZMADecompressor()
ret = dec.decompress(data1)
print(ret)
print(len(ret))
print(dec.unconsumed_tail)
ret = dec.decompress(data2)
print(ret)
print(len(ret))
print(dec.unconsumed_tail)
ret = dec.decompress(data3)
print(ret)
print(len(ret))
print(dec.unconsumed_tail)

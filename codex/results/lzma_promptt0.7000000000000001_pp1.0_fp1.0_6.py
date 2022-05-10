import lzma
# Test LZMADecompressor with data that has a dictionary size of 2^16
data = lzma.compress(b"x" * 2 ** 16, format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZMA1, "dict_size": 2 ** 16}])
assert len(data) == 14
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
# bytebuffer is not supported in Python 2.6
#b = bytearray(b"x" * 2 ** 16)
#decompressor.decompress(data, memoryview(b))
#assert b == b"x" * 2 ** 16
b = decompressor.decompress(data)
assert b == b"x" * 2 ** 16
# Test LZMADecompressor with data that has a dictionary size of 2^15
data = lzma.compress(b"x" * 2 ** 15, format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZ

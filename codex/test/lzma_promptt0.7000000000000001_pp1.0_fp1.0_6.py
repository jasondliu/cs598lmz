import lzma
# Test LZMADecompressor with data that has a dictionary size of 2^16
data = lzma.compress(b"x" * 2 ** 16, format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZMA1, "dict_size": 2 ** 16}])

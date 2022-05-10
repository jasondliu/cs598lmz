import lzma
# Test LZMADecompressor using a dictionary.

def roundtrip(x):
    d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZMA2, "dict_size": 1 << 12}])
    x2 = d.decompress(d.compress(x))
    assert x == x2


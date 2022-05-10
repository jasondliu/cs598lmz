import lzma
# Test LZMADecompressor using a dictionary.

def roundtrip(x):
    d = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZMA2, "dict_size": 1 << 12}])
    x2 = d.decompress(d.compress(x))
    assert x == x2

roundtrip(b"")
roundtrip(b"test")

# LZMA.FORMAT_XZ is only supported if the back-end supports it.
if hasattr(lzma, "FORMAT_XZ"):
    d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, filters=[{"id": lzma.FILTER_LZMA2, "dict_size": 1 << 12}])
    assert d.format == lzma.FORMAT_XZ
# Test LZMAFile using a dictionary.

def roundtrip(x):
    c = lzma.LZMAFile(io.BytesIO(),

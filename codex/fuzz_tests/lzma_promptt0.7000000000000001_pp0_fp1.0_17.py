import lzma
# Test LZMADecompressor with a dict_size of 0.
decompressor = lzma.LZMADecompressor(dict_size=0)
try:
    decompressor.decompress(b"")
except ValueError:
    pass
else:
    raise AssertionError("Dict size of 0 failed to raise ValueError")
# Test LZMADecompressor with a dict_size greater than the default.
default_dict_size = lzma._encode_dict_size(lzma.FORMAT_RAW, lzma.FILTER_LZMA1,
                                           0, lzma.FILTER_DELTA)
decompressor = lzma.LZMADecompressor(dict_size=default_dict_size + 1)
try:
    decompressor.decompress(b"")
except ValueError:
    pass
else:
    raise AssertionError(
        "Dict size of %i failed to raise ValueError" % (default_dict_size + 1)
    )
# Test LZMADecompressor with a dict

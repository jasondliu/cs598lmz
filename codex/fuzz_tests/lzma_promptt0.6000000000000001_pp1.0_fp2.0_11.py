import lzma
# Test LZMADecompressor.__init__()
#
# Test that the properties are set to the default values if no
# arguments are given.

decompressor = lzma.LZMADecompressor()

assert(decompressor.format == lzma.FORMAT_AUTO)
assert(decompressor.check == lzma.CHECK_UNKNOWN)
assert(decompressor.filters is None)
# Test LZMADecompressor.__init__()
#
# Test that the properties are set to the given values.

decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ,
                                     check=lzma.CHECK_CRC64,
                                     filters=[
                                         {"id": lzma.FILTER_LZMA2,
                                          "preset": 9 | lzma.PRESET_EXTREME}])

assert(decompressor.format == lzma.FORMAT_XZ)
assert(decompressor.check == lzma.CHECK_CRC64)
assert

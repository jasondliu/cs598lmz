import lzma
# Test LZMADecompressor.__init__()
data = b"test\000data"

# Valid properties and a first byte, these should all work
LZMADecompressor(lzma.FILTER_LZMA1, lzma.CHECK_NONE, properties=lzma._encode_filter_properties([]) + b"\0")
LZMADecompressor(lzma.FILTER_LZMA2, lzma.CHECK_NONE, properties=lzma._encode_filter_properties([]) + b"\0")
LZMADecompressor(lzma.FILTER_DELTA, lzma.CHECK_NONE, properties=lzma._encode_filter_properties([b"\0"]))
LZMADecompressor(lzma.FILTER_X86, lzma.CHECK_NONE, properties=lzma._encode_filter_properties([b"\0"]))
LZMADecompressor(lzma.FILTER_IA64, lzma.CHECK_NONE, properties=lz

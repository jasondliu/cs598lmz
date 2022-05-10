import lzma
# Test LZMADecompressor's readfrom() method and LZMAFile's .read() method
# together; this simulates the common case where it is not known whether
# the LZMA data has an end-of-stream marker
comp = lzma.LZMACompressor()
compressed = comp.compress(b"hello") + comp.compress(b"world")
decomp = lzma.LZMADecompressor()
data = decomp.decompress(compressed)
print(data)
# Test LZMADecompressor's readfrom() method and LZMAFile's read() method
# together; this simulates the case where the LZMA data is known to
# not have an end-of-stream marker
comp = lzma.LZMACompressor(format=lzma.FORMAT_RAW,
                           filters=[{"id":lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}])
compressed = comp.compress(b"hello") + comp.compress(b"world")
decomp

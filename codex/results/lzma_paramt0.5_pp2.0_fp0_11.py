from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

#lzma.decompress(compressed)

#lzma.decompress(compressed, format=lzma.FORMAT_ALONE)

#lzma.decompress(compressed, format=lzma.FORMAT_XZ)

#lzma.decompress(compressed, format=lzma.FORMAT_RAW)

#lzma.decompress(compressed, format=lzma.FORMAT_AUTO)

#lzma.decompress(compressed, format=lzma.FORMAT_AUTO, memlimit=1 << 20)

#lzma.decompress(compressed, format=lzma.FORMAT_AUTO, memlimit=1 << 20, filters=[
#    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
#    {"id": lzma.FILTER_DELTA, "dist": 5},
#])

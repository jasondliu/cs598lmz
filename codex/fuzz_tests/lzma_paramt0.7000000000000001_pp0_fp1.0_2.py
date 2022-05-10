from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# and a more complicated example using a filter chain
from lzma import LZMACompressor
compressor = LZMACompressor(format=FORMAT_ALONE, filters=[{"id":FILTER_LZMA2, "preset":3}, {"id":FILTER_X86}, {"id":FILTER_DELTA}])
compressor.compress(b"hello world!\n") + compressor.flush()

# decompressing an .xz file (with no header, hence FORMAT_RAW)
compressor = LZMACompressor(format=FORMAT_RAW, filters=[{"id":FILTER_LZMA2, "preset":3}, {"id":FILTER_X86}, {"id":FILTER_DELTA}])
compressor.compress(b"hello world!\n") + compressor.flush()

# decompressing an .xz file (with no header, hence FORMAT_RAW)
from lzma import LZMADecompressor
decompressor = LZMADecompressor(format=FORMAT_

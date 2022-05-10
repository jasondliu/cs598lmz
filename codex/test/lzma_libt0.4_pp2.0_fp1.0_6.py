import lzma
lzma.LZMAError

from lzma import LZMACompressor, LZMADecompressor

compressor = LZMACompressor()
compressor.compress(b'Hello World!')
compressor.flush()

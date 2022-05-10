from lzma import LZMADecompressor
LZMADecompressor().decompress(b'').decode('utf-8')

from lzma import LZMACompressor

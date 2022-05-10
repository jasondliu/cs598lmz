from lzma import LZMADecompressor
LZMADecompressor().decompress(b'').decode('utf-8')

from lzma import LZMACompressor
LZMACompressor().compress(b'').decode('utf-8')

from zlib import compress
compress(b'').decode('utf-8')

from zlib import decompress
decompress(b'').decode('utf-8')

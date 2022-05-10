from lzma import LZMADecompressor
LZMADecompressor.decompress(b'')

import pyximport; pyximport.install()
import cython_lzma
cython_lzma.decompress(b'')
</code>


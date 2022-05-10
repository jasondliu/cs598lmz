from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xf6\x2c')

import lzma
lzma.open('/tmp/foo.xz')

# tarfile
import tarfile

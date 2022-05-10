import bz2
bz2.decompress(file_contents)

from bz2 import decompress
decompress(file_contents)

from bz2 import BZ2Decompressor
d = BZ2Decompressor()
d.decompress(file_contents)
d.flush()

import bz2
uncompressed_data = b''
decompressor = bz2.BZ2Decompressor()
for block in iter(lambda: file_contents, b''):
    uncompressed_data += decompressor.decompress(block)
uncompressed_data += decompressor.flush()

import lzma
lzma.decompress(file_contents)

from lzma import decompress
decompress(file_contents)

from lzma import LZMADecompressor
d = LZMADecompressor()
d.decompress(file_contents)

import lzma
uncompressed_data = b''
decompressor = lzma.LZMADecompressor()
for block

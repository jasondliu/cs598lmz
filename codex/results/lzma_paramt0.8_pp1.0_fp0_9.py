from lzma import LZMADecompressor
LZMADecompressor()

from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()

import gzip
f = gzip.open('f.zip', 'rb')
file_content = f.read()

print(file_content)

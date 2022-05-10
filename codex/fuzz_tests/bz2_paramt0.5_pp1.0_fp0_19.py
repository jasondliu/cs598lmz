from bz2 import BZ2Decompressor
BZ2Decompressor

from __future__ import print_function

from bz2 import BZ2File
from bz2 import BZ2Compressor
from bz2 import BZ2Decompressor

from bz2 import compress
from bz2 import decompress
from bz2 import open as bz2_open

print('bz2:', bz2.__file__)
print('BZ2File:', BZ2File)
print('BZ2Compressor:', BZ2Compressor)
print('BZ2Decompressor:', BZ2Decompressor)
print('compress:', compress)
print('decompress:', decompress)
print('open:', bz2_open)

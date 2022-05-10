from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
 
# or with a decompressor object
decompressor = LZMADecompressor()
decompressor.decompress(data1)
decompressor.decompress(data2)

# or by using a context manager that handles the decompressor object
# for you
with lzma.open(filename, mode='rb') as file:
    file_content = file.read()
"""

from _lzma import *

from _lzma import __doc__

__version__ = _lzma.LZMA_VERSION_STRING

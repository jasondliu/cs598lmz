import lzma
lzma2compress = lzma.compress
lzma2decompress = lzma.decompress

try:
    import zlib
    zlibcompress = zlib.compress
    zlibdecompress = zlib.decompress
except ImportError:
    # Attempt to use zlib instead.
    # This is removed from the standard python libraries, but is available on PyPI.
    # See: https://pypi.python.org/pypi/zlib for more details.
    # In this case, the code will only work with pypy and cpython >= 3.3
    from zlib import compress as zlibcompress
    from zlib import decompress as zlibdecompress

# http://stackoverflow.com/questions/5387299/python-pil-ioerror-decoder-zip-not-available
Image.init()

#import pymouse
#import pykeyboard
#import pyscreenshot
#import sklearn

# The io module is used to control child process
import io
import struct

# This

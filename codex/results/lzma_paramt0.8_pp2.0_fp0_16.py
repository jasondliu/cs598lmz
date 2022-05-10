from lzma import LZMADecompressor
LZMADecompressor().decompress(b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x04J\x00;').decode('utf-8')  # doctest: +SKIP

"""

from array import array

from _lzma import *

# enum is not available in Python < 3.4
class ACTION(IntEnum):
    RUN = 0
    SYNC_FLUSH = 1
    FULL_FLUSH = 2
    FINISH = 3

def is_buffer(obj):
    # check that obj is a readable buffer (e.g. bytes or array)
    try:
        memoryview(obj)
    except TypeError:
        return False
    else:
        return True

class LZMACompressor(object):
    """A streaming LZMA compressor object.

    To compress data, create an LZMACompressor object, then call
    its compress() or compress1() method one or more times, with
    string data as parameter. The compres() method returns

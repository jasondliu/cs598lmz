from bz2 import BZ2Decompressor
BZ2Decompressor.decompress

## http://pecl.php.net/package/bzip2
## http://bugs.python.org/issue6551
## http://trac.osgeo.org/gdal/ticket/3368

##-----------------------------------------------------------------------------

class BZ2Compressor(object):
    '''
    >>> dat = b'1234567890'
    >>> bz2compress(dat)
    'BZh91AY&SY\xbd\xba\x00\x00\x00\x08\x00\x01\x04\x00\x00\x00\x00\x00\x00'
    >>> bz2decompress(bz2compress(dat))
    '1234567890'
    '''

    def __init__(self, compresslevel=9, bufsize=None):
        self._compresslevel = compresslevel
        self._bufsize = bufsize
        self._buf = b''
        self._compressor = BZ2Compressor(compresslevel)

    def compress(self, data):


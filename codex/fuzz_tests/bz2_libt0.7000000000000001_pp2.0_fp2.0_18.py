import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress


class LZMAFile(object):
    def __init__(self, filename=None, mode=None,
                 format=None, check=-1, preset=None, filters=None):
        if mode is None:
            if filename is None:
                mode = 'rb'
            else:
                mode = 'r'
        mode = mode.replace('b', '')
        if mode not in ('r', 'w', 'a'):
            raise ValueError("mode must be 'r', 'w' or 'a'")
        if format is not None and format != 'xz':
            raise ValueError("format must be None or 'xz' (not %r)" % format)

        self._mode = mode

        if mode == 'r':
            self._decompressor = LZMADecompressor()
            self._readbuffer = b''
            self._size = -1
            if filename is None:
                self._fp = io.BufferedReader(

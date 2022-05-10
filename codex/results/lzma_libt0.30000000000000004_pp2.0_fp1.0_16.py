import lzma
lzma.open

class LZMAFile(io.BufferedIOBase):
    """
    A file object providing transparent reading or writing of data
    compressed with the LZMA algorithm.
    """

    def __init__(self, filename, mode="r", *, fileobj=None, preset=None, filters=None):
        if mode not in ("r", "w", "x", "a"):
            raise ValueError("mode must be 'r', 'w', 'x' or 'a'")
        if fileobj is not None and filename is not None:
            raise ValueError("filename and fileobj cannot both be specified")
        if fileobj is None:
            fileobj = self._open(filename, mode)
        self._fileobj = fileobj
        self._mode = mode
        self._size = -1
        self._pos = 0
        self._buffer = b""
        self._eof = False
        self._closed = False
        self._preset = preset
        self._filters = filters

    def readable(self):
        return self._mode in ("r",

import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None): # real signature unknown; restored from __doc__
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """ fileno(self) -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """ isatty(self) -> bool """
        return False

    def readable(self): # real signature unknown; restored from __doc__
        """ readable(self) -> bool """
        return False

    def readline(self, limit=-1): # real signature unknown; restored from __doc__
        """ readline(self, limit: int = -1) -> str """
        return ""

    def writable(self): # real signature unknown; restored from __doc__
        """ writable(self) -> bool """


import io
class File(io.RawIOBase):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.file = None
        if opener:
            self.file = opener(path, mode, buffering)
        else:
            self.file = open(path, mode, buffering)
    #----------------------------------------------------------------------
    def __enter__(self):
        return self.file
    #----------------------------------------------------------------------
    def __exit__(self, *args):
        self.file.close()
class PyFile(io.RawIOBase):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        """"""
        if path in sys.builtin_module_names:
            raise ValueError("Invalid filename: %s" % path)
        self._handle = None
        self._close = closefd


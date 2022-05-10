import io
class File(io.RawIOBase):
    """Text I/O implementation using foundaion.NSFileHandle.
    
    The difference between this and the 'new' file object is that this
    version is not a subclass of the builtin file object.  This will
    eventually be deprecated.  The API of this should be considered
    identical to the builtin object.

    The 'encoding' parameter defaults to the encoding attribute of the
    base 'f' attribute.
    """
    def __init__(self, f, mode='U', encoding=None):
        self._file_handle = f
        if (mode and mode[0] == 'r') and (not hasattr(self,'_file_handle')):
            self._file_handle = f.open(mode.replace("b",""), encoding=encoding)
        self._mode = mode
        if self._mode.endswith("b"):
            self._is_binary = True
        else:
            self._is_binary = False
        self._line_number = 0
        if self._is_binary:
            self._buffer = b''
        else:
           

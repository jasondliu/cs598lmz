import io
class File(io.RawIOBase):
    __qualname__ = 'File'
    _CHUNK_SIZE = 512
    _MODE_BINARY = 0
    _MODE_TEXT = 1
    _NEWLINE_CONVERTER = None
    _UNIVERSAL_NEWLINES = 0
    _CHUNK_SIZE = 512
    encoding = None
    errors = None
    name = None
    mode = None

    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        if self.opener is not None:
            if buffering < 0:
                buffering = io.DEFAULT_BUFFER_SIZE
            if buffering < 0:
                buffering = io.DEFAULT_BUFFER_SIZE
            if buffering < 0:
                buffering = io.DEFAULT_BUFFER_SIZE
            if buffering < 0:
                buffering = io.

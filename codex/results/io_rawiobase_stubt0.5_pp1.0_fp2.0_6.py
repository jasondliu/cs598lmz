import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.mode = mode
        self.name = path
        self.encoding = encoding
        self.errors = errors
        self.open(path, mode, buffering, encoding, errors, newline, closefd, opener)
        

    def open(self, path, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True, opener=None):
        self.close()
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering < 0:
            raise ValueError("invalid buffering size")
        if not set(mode) <= set("arwb+tU"):
            raise ValueError("invalid mode: %r" % (mode,))
        if 'U' in mode:
            raise ValueError("universal newlines mode is not supported in py3k")
        creating

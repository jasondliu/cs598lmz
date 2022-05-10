import io
class File(io.RawIOBase):

    def __init__(self, fd):
        self.closed = False
        self.fd = fd
        self.mode = io.DEFAULT_BUFFER_SIZE

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be read. """
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be seeked. """
        pass

    def tell(self, *args, **kw

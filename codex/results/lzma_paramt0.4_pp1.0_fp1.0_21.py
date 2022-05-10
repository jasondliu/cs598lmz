from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''

class LZMAFile(object):
    def __init__(self, filename, mode='rb'):
        self.filename = filename
        self.mode = mode
        self.fileobj = None
        self.decompressor = None
        self.eof = False
        self.pos = 0
        self.size = -1
        self.closed = False
        self.exception = None

    def read(self, size=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if self.eof:
            return b''
        if self.exception is not None:
            raise self.exception
        if self.fileobj is None:
            try:
                self.fileobj = open(self.filename, self.mode)
                self.decompressor = LZMADecompressor()
            except Exception as e:
                self.exception = e
                raise
        if size == -1:
            size = 1024 * 1024
        data = b''
        while True

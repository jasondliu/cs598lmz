import weakref

class Reader:

    def __init__(self, file):
        self.file = file
        self.buf = ''
        self.byte_count = 0

    @property
    def position(self):
        return self.byte_count

    def read(self, size=None):
        """ Reads the given number of bytes, or until the end of the file """
        if size is None:
            size = sys.maxint
        if len(self.buf) < size:
            self.buf += self.file.read(size - len(self.buf))
            if not self.buf:
                raise EOFError()
        data = self.buf[:size]
        self.buf = self.buf[size:]
        self.byte_count += len(data)
        return data

    def readline(self, limit=None):
        """ Reads one line of bytes, with the given limit """
        if limit is None:
            limit = self.byte_count
        self.buf += self.file.readline(limit)
        if not self.buf:

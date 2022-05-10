import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Reader:
    """
    Wrapper around a file object with a special readline() method.
    """
    def __init__(self, file, encoding='utf-8', errors='replace'):
        self.file = file
        self.encoding = encoding
        self.errors = errors
        self.buf = b''
        self.eol = True

    def readline(self, size=-1):
        """
        Reads a full line from the file.
        """
        if size == -1:
            size = sys.maxsize
        if self.eol:
            self.buf = b''
        while not self.eol:
            self.buf += self.file.read(1)
            self.eol = self.buf[-1] == b'\n'
            if len(self.buf) >= size:
                self.eol = True
        ret = self.buf
        self.buf = b''
        return ret.decode(self.encoding, self.errors)

   

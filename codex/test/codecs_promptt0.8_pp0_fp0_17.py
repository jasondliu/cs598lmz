import codecs
# Test codecs.register_error(<name>)
from codecs import register_error
register_error('test', codecs.lookup_error('replace'))
from io import BytesIO
# Test io.BufferedIOBase.write() and io.BufferedIOBase.writable()
from io import BufferedIOBase
from io import UnsupportedOperation as UO
import encodings.latin_1

class TestBuffer:
    "Canonical test cases for BufferedIOBase implementations."

    def __init__(self, init=b'', encoding=None):
        self.encoding = encoding
        self.buf = []
        self.extend(init)

    def getvalue(self):
        return b''.join(self.buf)

    def close(self):
        pass

    def seekable(self):
        return False

    def readable(self):
        return True

    def writable(self):
        return True

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def readlines(self):
        rv = []


import io
class File(io.RawIOBase):
    name = 'adb'
    mode = 'r+b'
    encoding = None
    _writable = True
    _readable = True
    _blocking = True
    def __init__(self):
        self.file = io.BytesIO()
    def readable(self):
        return self._readable
    def writable(self):
        return self._writable
def read(self, size=-1):
    if self.closed:
        raise ValueError('I/O operation on closed file.')
    return None
def readlines(self, hint=None):
    if self.closed:
        raise ValueError('I/O operation on closed file.')
    return None
def readline(self, size=-1):
    if self.closed:
        raise ValueError('I/O operation on closed file.')
    return None
def write(self, data):
    for i in data:
        if i == '\n': i = '\r\n'
        c.write(i)
def __del__(self):
    c.close()
    print

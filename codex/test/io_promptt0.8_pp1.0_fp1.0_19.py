import io
# Test io.RawIOBase
class MyIO(io.RawIOBase):
    def __init__(self, content):
        self._content = content

    def read(self, n=-1):
        if not self._content:
            return ''
        elif n >= 0:
            return self._content.pop(0)
        else:
            return self._content.pop()

    def write(self, s):
        self._content.append(s)
        return len(s)

    def isatty(self):
        return False

# Test BufferedWriter
class MyBufferedWriter(io.BufferedWriter):
    def __init__(self, f):
        io.BufferedWriter.__init__(self, f)
        self.additional_attributes = 'test'

# Test io.BufferedReader
class MyBufferedReader(io.BufferedReader):
    def read1(self, n):
        self._read_buf = None
        return io.BufferedReader.read(self, n)

# Test io.BufferedRandom

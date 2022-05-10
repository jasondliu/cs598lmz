import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def close(self):
        self.f.close()
    def fileno(self):
        return self.f.fileno()

f = open('test.txt', 'rb')
f2 = io.BufferedReader(File(f))
print(f2.read())
f2.close()

"""
io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)
io.BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)
io.BufferedRWPair(reader, writer, buffer_size=DEFAULT_BUFFER_SIZE)
io.BufferedRandom(raw, buffer_size=DEFAULT_BUFFER_SIZE)
"""

"""
io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buff

import io
class File(io.RawIOBase):
    def __init__(self, fh):
        self.fh = fh
        self.line_buffer = b''
        self.line_buffer_used = 0
        self.pos = 0

    def read(self, size=-1):
        if size &lt; 0:
            return self.readall()

        result = self.line_buffer[self.line_buffer_used:self.line_buffer_used + size]
        if len(result) &lt; size:
            result += self.fh.read(size - len(result))
        self.pos += len(result)
        self.line_buffer_used += len(result)
        return result

    def readable(self):
        return True

    def readall(self):
        b = self.read(self.line_buffer_used + 1024)
        if len(b) &lt;= self.line_buffer_used:
            return b
        return b[:-1]

    def readline(self, size=-1):
        data = bytearray()
        while len(

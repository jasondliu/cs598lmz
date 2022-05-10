import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.encoding = 'utf-8'
        self.buffer = ''
        self.line_buffer = ''
    def readable(self):
        return True
    def readline(self, limit=-1):
        while '\n' not in self.line_buffer and (limit < 0 or len(self.line_buffer) < limit):
            chunk = self.read(limit - len(self.line_buffer))
            if not chunk:
                break
            self.line_buffer += chunk
        sio = io.StringIO(self.line_buffer)
        if limit < 0:
            line = sio.readline()
        else:
            line = sio.readline(limit)
        self.line_buffer = self.line_buffer[sio.tell():]
        return line
    def read(self, n=-1):
        while len(self.buffer) < n or n < 0:
            chunk = self.file.read(n - len(self.buffer))
           

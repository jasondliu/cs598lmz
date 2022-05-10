import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, 'r')
        self.buf_size = 1024
        self.buffer = self.file.read(self.buf_size)
        self.buf_end = 0
        self.buf_pos = 0

    def read(self, n=-1):
        if n >= 0:
            if n <= self.buf_end - self.buf_pos:
                data = self.buffer[self.buf_pos:self.buf_pos + n]
                self.buf_pos += n
                return data
            else:
                data = self.buffer[self.buf_pos:]
                self.buf_pos = self.buf_end
                while True:
                    self.buffer = self.file.read(self.buf_size)
                    self.buf_end = len(self.buffer)
                    if self.buf_end == 0:
                        return data
                    need = n - len(data)
                    data += self.buffer[:need]
                    self.

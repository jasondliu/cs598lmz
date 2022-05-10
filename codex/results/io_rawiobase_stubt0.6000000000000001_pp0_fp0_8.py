import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.name = filename
        self.file = filename
        self.mode = 'w'
        self.encoding = 'utf-8'
        self.errors = None
        self.newlines = None
        self.closed = False
        self.write_data = ''
        self.read_data = ''
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            return self.read_data
        else:
            data = self.read_data[size:]
            self.read_data = self.read_data[:size]
            return data

    def readline(self, size=-1):
        if size == -1:
            return self.read_data
        else:
            data = self.read_data[size:]
            self.read_data = self.read_data[:size]
            return data

    def write(self, b):
        self.write_data += b
        return len(b)

    def close(self):
       

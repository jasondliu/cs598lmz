import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        self.buffer = b''
    def read(self, size):
        if size == -1:
            data = self.buffer + self.file.read()
            self.buffer = b''
            return data
        while len(self.buffer) < size:
            data = self.file.read(size - len(self.buffer))
            if not data:
                break
            self.buffer += data
        data, self.buffer = self.buffer[:size], self.buffer[size:]
        return data
    def write(self, data):
        return self.file.write(data)
    def seek(self, offset, whence=0):
        if whence == 1:
            offset = self.tell() + offset
        elif whence == 2:
            offset = self.file.seek(0, 2) + offset
        if offset < len(self.buffer):
            self.buffer = self.buffer[

import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = io.open(filename, 'rb')
        self.size = os.fstat(self.file.fileno()).st_size
        self.pos = 0

    def read(self, size):
        if self.pos + size > self.size:
            size = self.size - self.pos
        if size == 0:
            return b''
        self.pos += size
        return self.file.read(size)

    def tell(self):
        return self.pos

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.size + pos
        else:
            raise ValueError("Invalid value for `whence`")
        return self.pos

    def close(self):
        self.file.close()

def get_audio_data(filename):
    f = File(filename

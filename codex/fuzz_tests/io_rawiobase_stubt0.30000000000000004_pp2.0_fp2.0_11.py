import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.pos = 0
        self.size = 0
        self.open()
    def open(self):
        if self.file is None:
            self.file = open(self.file_name, self.mode)
            self.size = os.path.getsize(self.file_name)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        if self.file is None:
            self.open()
        self.file.seek(self.pos)
        num_read = self.file.readinto(b)
        self.pos += num_read
        return num_read
    def write(self, b):

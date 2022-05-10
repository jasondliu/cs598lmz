import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_size = os.path.getsize(self.file_path)
        self.position = 0
    def readable(self):
        return True
    def readinto(self, b):
        if self.file is None:
            self.file = open(self.file_path, 'rb')
        if self.position >= self.file_size:
            return None
        self.file.seek(self.position)
        size_to_read = min(len(b), self.file_size - self.position)
        result = self.file.readinto(b[:size_to_read])
        self.position += size_to_read
        return result
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.position = offset
        elif whence == 1:
            self.position += offset
        elif whence == 2:

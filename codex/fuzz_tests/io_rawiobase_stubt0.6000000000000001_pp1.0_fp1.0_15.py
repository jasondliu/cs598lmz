import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.file = open(file_path, 'rb')
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            return self.file.read()

        if self.pos + size > self.file_size:
            size = self.file_size - self.pos
            self.pos = self.file_size
            return self.file.read(size)

        self.pos += size
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.pos += offset
        elif whence == io.SEEK_END:
            self.pos = self.file_size + offset
        self.file.seek(self.pos

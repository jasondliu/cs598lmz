import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.f = None
        self.f_size = None
        self.f_offset = 0

    def open_file(self):
        if self.f is None:
            self.f = open(self.file_path, 'rb')
            self.f_size = os.path.getsize(self.file_path)

    def close(self):
        if self.f is not None:
            self.f.close()
            self.f = None

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return False

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.f_offset = offset
        elif whence == io.SEEK_CUR:
            self.f_offset += offset
        elif whence == io.SEEK_END:
            self.f_offset = self

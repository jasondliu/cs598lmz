import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.is_open = False

    def open(self):
        if self.is_open:
            raise ValueError('File is already open')
        self.file = open(self.file_name, self.mode)
        self.is_open = True

    def close(self):
        if not self.is_open:
            raise ValueError('File is not open')
        self.file.close()
        self.is_open = False

    def read(self, n=-1):
        if not self.is_open:
            raise ValueError('File is not open')
        return self.file.read(n)

    def write(self, b):
        if not self.is_open:
            raise ValueError('File is not open')
        self.file.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        if not

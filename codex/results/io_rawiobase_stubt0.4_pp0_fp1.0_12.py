import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        self.file_obj = None
        self.closed = True

    def open(self):
        self.file_obj = open(self.file_name, self.mode)
        self.closed = False

    def close(self):
        if self.closed:
            return
        self.file_obj.close()
        self.closed = True

    def readable(self):
        return self.mode in ['r', 'r+', 'w+']

    def writable(self):
        return self.mode in ['w', 'w+', 'a', 'a+']

    def seekable(self):
        return True

    def readinto(self, b):
        return self.file_obj.readinto(b)

    def read(self, n=-1):
        return self.file_obj.read(n)

    def write(self, b):
        return self.file_obj.write(b)

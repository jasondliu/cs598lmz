import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self, n=-1):
        with open(self.file_name, 'rb') as file:
            return file.read(n)

    def readable(self):
        return True

    def writable(self):
        return False

# https://docs.python.org/3/library/io.html#io.RawIOBase
# https://docs.python.org/3/library/io.html#io.BufferedIOBase
class BufferedFile(io.BufferedIOBase):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'rb')

    def read(self, n=-1):
        return self.file.read(n)

    def readable(self):
        return True

    def writable(self):
        return False

    def close(self):
        self.file.close()

    def flush(self):
        pass



import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', block_size=io.DEFAULT_BUFFER_SIZE):
        self.path = path
        self.mode = mode
        if block_size is None:
            block_size = io.DEFAULT_BUFFER_SIZE
        self.block_size = block_size

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def __iter__(self):
        return self

    def __next__(self):
        data = self.readline()
        if data:
            return data
        raise StopIteration

    def read(self, n=None):
        if not self.readable():
            raise io.UnsupportedOperation("File not open for reading")
        with open(self.path, 'rb') as f:
            if n is None:
                return f.read()
            else:
                return f.read(n)

    def readline(self, limit

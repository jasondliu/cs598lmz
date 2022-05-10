import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self._f = io.open(filename, 'rb')
        self.filename = filename
    def read(self, n=-1):
        return self._f.read(n)
    def close(self):
        self.closed = True
        self._f.close()

if __name__ == "__main__":
    path = os.path.expanduser("./test_file_io.txt")
    with File(path) as f:
        print(f.read(20))
        print(f.closed)
    print(f.closed)
    print(hasattr(f, "closed"))
    #f.close()
    print(f.closed)
    print(hasattr(f, "closed"))

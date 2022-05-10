import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name

    def read(self, size=-1):
        if size == -1:
            size = os.path.getsize(self.name)
        return open(self.name, 'rb').read(size)

    def readinto(self, b):
        data = self.read(len(b))
        b[:len(data)] = data
        return len(data)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        open(self.name, 'rb').seek(offset, whence)

    def tell(self):
        return open(self.name, 'rb').tell()

if __name__ == '__main__':
    f = File('file.txt')
    print(f.read())

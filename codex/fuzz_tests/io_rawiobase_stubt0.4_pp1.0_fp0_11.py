import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        self.path = path
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.path, self.mode, *args, **kwargs)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def read(self, n=-1):
        return self.file.read(n)

    def tell(self):
        return self.file.tell()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

def main():
    with File('/tmp/test.txt', 'w') as f:
        f.write('hello world')
        f.seek(0)
        print(f.tell

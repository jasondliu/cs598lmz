import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

def open(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, str):
        return io.open(file, mode, buffering, encoding, errors, newline, closefd, opener)
    return io.TextIOWrapper(File(file), encoding, errors, newline)

def main():
    parser = argparse.ArgumentParser(description='Convert a binary file to a C array')
    parser.add_argument('-o', '--

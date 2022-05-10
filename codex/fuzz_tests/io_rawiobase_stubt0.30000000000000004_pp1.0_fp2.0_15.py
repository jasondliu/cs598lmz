import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self.fp = fp
    def read(self, n):
        return self.fp.read(n)
    def seek(self, n):
        self.fp.seek(n)
    def tell(self):
        return self.fp.tell()
    def close(self):
        self.fp.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def open(file, mode='r'):
    if mode == 'r':
        return File(io.open(file, 'rb'))
    elif mode == 'w':
        return File(io.open(file, 'wb'))
    else:
        raise ValueError('invalid mode')

def listdir(path):
    return os.listdir(path)

def mkdir(path):
    os.mkdir(path)

def remove(path):
    os.remove(path)



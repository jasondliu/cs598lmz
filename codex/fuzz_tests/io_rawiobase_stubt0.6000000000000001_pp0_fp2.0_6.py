import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
        self.name = name
    def readable(self):
        return False
    def writable(self):
        return False
    def seekable(self):
        return False
    def close(self):
        pass

class Wrapper:
    def __init__(self, file):
        self.file = file
    def __getattr__(self, name):
        return getattr(self.file, name)
    def __iter__(self):
        return self
    def __next__(self):
        return self.file.read()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return False

def myprint(*args, **kwargs):
    print(*args, **kwargs)

def open(name, mode='r', buffering=-1, encoding=None,

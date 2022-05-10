import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.f = open(self.path, self.mode)
        return self

    def __exit__(self, type, value, traceback):
        self.f.close()

with File('/tmp/hello.txt', 'w') as f:
    f.write('hello world')

# context manager with error handling
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.f = open(self.path, self.mode)
        return self

    def __exit__(self, type, value, traceback):
        self.f.close()
        return True

with File('/tmp/hello.txt', 'w') as f:
    raise ValueError()

# context manager using contextlib.contextmanager decorator
from contextlib import contextmanager

@

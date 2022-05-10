import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return self.f.fileno()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if newline is not None:
        raise ValueError("newline is not supported in py3k")
    if not closefd:
        raise ValueError("closefd is not supported in py3k")
    if opener is not None:
        raise ValueError("opener is not supported in py3k")
    return io.open(file, mode, buffering, encoding, errors)

import pickle
try:
    from cPickle import Pickler,

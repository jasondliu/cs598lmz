import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode

    def read(self, n=-1):
        return self._file.read(n)

    def readinto(self, b):
        data = self._file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n

    def write(self, b):
        self._file.write(b)
        return len(b)

    @property
    def closed(self):
        return self._file.closed

    def close(self):
        return self._file.close()

def open(file, mode='r'):
    return File(file, mode)

def main():
    import sys
    import pickle
    import random
    random.seed(1)

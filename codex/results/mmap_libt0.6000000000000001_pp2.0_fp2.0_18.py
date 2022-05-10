import mmap

from . import core
from . import consts


def default_progress_function(pct: float):
    print('{:.2f}%'.format(pct))


class File:
    def __init__(self, path: str, mode: str = 'r'):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, size: int = -1) -> bytes:
        if self.file is None:
            raise EnvironmentError('File is not opened')
        return self.file.read(size)

    def write(self, data: bytes):
        if self.file is None:
            raise EnvironmentError('File is not opened')
        self.file.write(data)

    def seek(self, offset: int, whence: int = 0):

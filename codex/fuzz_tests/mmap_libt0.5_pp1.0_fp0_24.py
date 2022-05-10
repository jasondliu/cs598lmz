import mmap

from . import utils

class File(object):
    def __init__(self, path, mode='w', encoding='utf-8'):
        self._path = path
        self._mode = mode
        self._encoding = encoding
        self._file = None
        self._mmap = None

    def __enter__(self):
        self._file = open(self._path, self._mode, encoding=self._encoding)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()

    def __len__(self):
        return os.path.getsize(self._path)

    def __iter__(self):
        self.seek(0)
        while True:
            line = self.readline()
            if not line:
                break
            yield line

    def seek(self, offset):
        if self._mmap:
            self._mmap.seek(offset)
        else:
            self._file.seek(offset)

    def tell(self):

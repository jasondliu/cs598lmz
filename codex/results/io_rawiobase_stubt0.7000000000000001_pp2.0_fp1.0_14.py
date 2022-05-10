import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        print('__init__')
        self.filename = filename
        self.mode = mode
        self.open_file = io.open(self.filename, self.mode)
        self._is_open = True

    def read(self, *args):
        print('read')
        return self.open_file.read(*args)

    def write(self, *args):
        print('write')
        return self.open_file.write(*args)

    def close(self, *args):
        print('close')
        self.open_file.close(*args)
        self._is_open = False

    def __enter__(self):
        print('__enter__')
        if not self._is_open:
            return self.open_file.__enter__()

    def __exit__(self, *args):
        print('__exit__')
        if self._is_open:
            return self.open_file.__exit__(*args)

with File('file.txt', 'w') as

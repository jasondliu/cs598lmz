import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._position = 0
        try:
            self._file = open(name, mode)
        except OSError:
            raise ValueError("Invalid file name or mode")
    def close(self):
        self._file.close()
    def read(self, n):
        if not self._mode.startswith('r'):
            raise ValueError("File not open for reading")
        if n is None:
            data = self._file.read()
        else:
            data = self._file.read(n)
        self._position += len(data)
        return data
    def seek(self, offset, whence=0):
        if whence == 0:
            new_position = offset
        elif whence == 1:
            new_position = self._position + offset
        elif whence == 2:
            new_position = -offset
        else:
            raise ValueError("Invalid value for 'whence'")
        if new_position < 0

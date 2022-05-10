import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._content = ''
        self._current = 0
        self._length = len(self._content)
    def read(self, count=-1):
        if count < 0:
            count = self._length
        if self._current + count > self._length:
            count = self._length - self._current
        if count > 0:
            data = self._content[self._current:self._current + count]
            self._current += count
            return data
        else:
            return b''
    def write(self, data):
        self._content += data
        self._length = len(self._content)
        return len(data)
    def flush(self):
        pass
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._current = offset
        elif whence == io.SEEK_CUR:
            self._current += offset
        elif whence ==

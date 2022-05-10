import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        self._buffer = b''
        super(File, self).__init__(*args, **kwargs)

    def readable(self):
        return True

    def _read(self, size=-1):
        while size == -1 or size > len(self._buffer):
            self._buffer += self._file.read(1024)
        r, self._buffer = self._buffer[:size], self._buffer[size:]
        return r

    def read(self, size=-1):
        return self._read(size)

    def readinto(self, b):
        data = self._read(len(b))
        b[:len(data)] = data
        return len(data)

    def readline(self, size=-1):
        if size < 0:
            size = None
        while b'\n' not in self._buffer and \
              (size is None or len(self._buffer) < size):
            if size:
                # since size is not

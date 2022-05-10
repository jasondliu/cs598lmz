import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self._file = open(filename, mode='rb')
        self._buffer = b''
        self._buffer_size = 0
        self._buffer_pos = 0
    def _fill_buffer(self):
        if self._buffer_size == 0:
            self._buffer_size = self._file.readinto(self._buffer)
            self._buffer_pos = 0
    def readinto(self, b):
        self._fill_buffer()
        if self._buffer_size > 0:
            n = min(len(b), self._buffer_size - self._buffer_pos)
            b[:n] = self._buffer[self._buffer_pos:self._buffer_pos+n]
            self._buffer_pos += n
            return n
        return 0
    def readable(self):
        return True
    def close(self):
        self._file.close()
        self._buffer_size = 0
        self._buffer_pos = 0

def read_file(filename):
    with File(filename) as f

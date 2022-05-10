import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self._name = name
        self._mode = mode
        self._closefd = closefd
        self._fd = None
        self._open()

    def _open(self):
        self._fd = os.open(self._name, self._mode)

    def close(self):
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None

    def readable(self):
        return self._mode in ('r', 'r+', 'a+')

    def writable(self):
        return self._mode in ('w', 'w+', 'a', 'a+')

    def seekable(self):
        return True

    def _check_open(self):
        if self._fd is None:
            raise ValueError("I/O operation on closed file")

    def _adjust_pos(self, pos):
        if pos is None:
            return self.tell()
        elif pos < 0:
            return max(0,

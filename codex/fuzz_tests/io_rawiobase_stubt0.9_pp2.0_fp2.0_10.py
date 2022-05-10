import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode='r', size=1024 ** 2, bias=0, offset=0, detached=False):
        if 'b' in mode:
            self.mode = mode
        else:
            self.mode = mode + 'b'

        self.filepath = filepath
        self.size = size
        self.bias = bias
        self.offset = offset
        self.detached = detached
        # super(File, self).__init__()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()
        return False

    def open(self):
        self._fd = io.open(self.filepath, self.mode, buffering=self.size)
        if self.bias > 0:
            start = self.bias // self.size * self.size
            start = start if start >= 0 else 0
            self._fd.seek(start)
        self._last_offset = self._fd.tell()
        self._

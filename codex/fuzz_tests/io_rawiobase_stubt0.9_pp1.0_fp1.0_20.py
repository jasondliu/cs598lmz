import io
class File(io.RawIOBase):
    def _open(self, filename, mode):
        self._filename = filename
        self._mode = mode
        self._file = open(filename, mode)
        return self

    def fileno(self):
        return self._file.fileno()

    def close(self):
        if not self.closed:
            self._file.close()
            self._file = None
            super(File, self).close()

    def isatty(self):
        return self._file.isatty()

    # RawIOBase methods

    def read(self, n): return self._file.read(n)

    def readall(self): return self._file.readall()

    def readable(self): return self._file.readable()

    def readinto(self, b): return self._file.readinto(b)

    def readline(self): return self._file.readline()

    def seek(self, pos, whence=0): self._file.seek(pos, whence)

    def seekable(self): return self._file.seekable()

    def tell(self

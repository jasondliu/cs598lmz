import io
class File(io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def _check_file(self):
        if not self.file:
            raise ValueError("I/O operation on closed file")

    def _read_block(self):
        self._check_file()
        self.blocksize = self.file.read(BLOCKSIZE)
        assert len(self.blocksize) == BLOCKSIZE

    def _write_block(self):
        self._check_file()
        self.file.write(self.blocksize)

    def read(self, n=-1):
        self._check_file()

        if n == -1:
            out = []
            while True:
                self._read_block()
                if self._pos >= BLOCKSIZE:
                    break
                out.append(self.blocksize[self._pos])
                self._pos += 1
            s = ''.join(out)
            return s

        elif n > -1:
            out = []

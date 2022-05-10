import io
class File(io.RawIOBase):

    def __init__(self, file, *args, **kwargs):
        self._file = file
        super(File, self).__init__(*args, **kwargs)

    def close(self):
        return self._file.close()

    def fileno(self):
        return self._file.fileno()

    def isatty(self):
        return self._file.isatty()

    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self._file.tell()


class BufferedWriter(io.BufferedWriter):

    def __init__(self, raw, buffer_size=io.DEFAULT_BUFFER_SIZE):
        super(BufferedWriter, self).__init__(raw, buffer_size)

    def write(self, b):
        self.raw.write(b)

class BufferedReader(io.BufferedReader):

    def __

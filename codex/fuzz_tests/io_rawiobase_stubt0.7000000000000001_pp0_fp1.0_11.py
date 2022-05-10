import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self._read_file()

    def _read_file(self):
        with open(self.file_path, 'r') as f:
            self.buffer = f.read()
            self.buffer_len = len(self.buffer)
            self.buffer_start = 0
            self.buffer_end = self.buffer_len

    def read(self, size=-1):
        if size == -1:
            size = self.buffer_len - self.buffer_start
        self.buffer_start += size
        return self.buffer[self.buffer_start-size:self.buffer_start]

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            if offset < 0:
                offset = 0
            elif offset > self.buffer_len:
                offset = self.buffer_len
            self.buffer_start = offset
        elif whence == io.SEEK_CUR:


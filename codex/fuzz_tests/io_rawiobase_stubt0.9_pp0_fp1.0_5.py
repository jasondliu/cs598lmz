import io
class File(io.RawIOBase):
    __qualname__ = 'File'
    LINEFEED = b'\n'
    ALLOCATION_BLOCK = 4096
    def __init__(self, fd, mode=None):
        super().__init__()
        self.fd = fd
        self.name = fd.getName()
        self.mode = mode
        self._read_buf = []
        self._read_buf_offset = 0
        self._read_buf_pos = 0
        self._read_buf_len = 0
        self._write_buf = []
        self._write_pos = 0
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._read_buf_offset = offset
            self._read_buf = []
            self._read_buf_pos = 0
            self._read_buf_len = []
            self._fseek(offset)
        elif whence == io.SEEK_CUR:
            self._read_buf_offset += offset
            self._fseek(self

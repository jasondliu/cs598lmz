import io
class File(io.RawIOBase):
    """A file-like object that reads and writes from the file descriptor fd.

    The file descriptor fd must be opened in binary mode.
    """

    def __init__(self, fd):
        self._fd = fd
        self._read_buf = b""
        self._write_buf = b""

    def readinto(self, b):
        if self._read_buf:
            # copy as much as we can from read buffer
            chunk = self._read_buf[:len(b)]
            b[:len(chunk)] = chunk
            self._read_buf = self._read_buf[len(chunk):]
            return len(chunk)
        else:
            return os.read(self._fd, len(b))

    def write(self, b):
        if self._write_buf:
            # append to write buffer
            self._write_buf += b
        else:
            # try to write directly from b
            try:
                n = os.write(self._fd, b)
            except BlockingIOError:
               

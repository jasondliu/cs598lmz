import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r", bufsize=-1):
        self._file = file
        self._mode = mode
        self._bufsize = bufsize
        self._wbuf = bytearray()
        self._rbuf = bytearray()
        self._rbuf_len = 0
        self._rbuf_pos = 0
        self._rbuf_end = 0
        self._read_lock = threading.Lock()
        self._write_lock = threading.Lock()
        self._seek_lock = threading.Lock()
        self._seekable = file.seekable()
        if self._seekable:
            self._seek_lock.acquire()
            self._file.seek(0, io.SEEK_END)
            self._rbuf_end = self._file.tell()
            self._seek_lock.release()
    def readinto(self, b):
        with self._read_lock:
            if self._rbuf_len == 0:
                if self._seekable:
                    self._seek_lock.

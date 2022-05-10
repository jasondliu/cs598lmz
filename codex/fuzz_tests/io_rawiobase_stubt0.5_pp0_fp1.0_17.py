import io
class File(io.RawIOBase):
    def __init__(self, path, flags=0, mode=0o777):
        self._path = path
        self._flags = flags
        self._mode = mode
        self._handle = -1
        self._open()

    def _open(self):
        if self._handle != -1:
            return
        self._handle = lib.f_open(self._path, self._flags, self._mode)
        if self._handle < 0:
            raise OSError(errno.errorcode[-self._handle], self._path)

    def close(self):
        if self._handle != -1:
            ret = lib.f_close(self._handle)
            self._handle = -1
            if ret < 0:
                raise OSError(errno.errorcode[-ret], self._path)

    def fileno(self):
        return self._handle

    def isatty(self):
        return False

    def readable(self):
        return self._flags & os.O_RDONLY == os.O_RDONLY

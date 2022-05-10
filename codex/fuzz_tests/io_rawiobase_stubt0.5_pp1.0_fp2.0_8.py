import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r"):
        super().__init__()
        self._name = name
        self._mode = mode
        self._f = None
        self._f_no = None

    def __repr__(self):
        return "{}('{}', '{}')".format(type(self).__name__, self._name, self._mode)

    def __str__(self):
        return repr(self)

    @property
    def name(self):
        return self._name

    @property
    def mode(self):
        return self._mode

    def close(self):
        if self._f is not None:
            self._f.close()
            self._f = None

    def fileno(self):
        if self._f is None:
            self._f = open(self._name, self._mode)
            self._f_no = self._f.fileno()
        return self._f_no

    def seekable(self):
        return True

    def readable(self):
        return

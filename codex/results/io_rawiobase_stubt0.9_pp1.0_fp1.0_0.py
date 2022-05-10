import io
class File(io.RawIOBase):
    def __init__(self, name, mode='rb', buffering=-1, encoding='utf-8',
                 errors='strict', newline=None, closefd=True):
        io.RawIOBase.__init__(self)
        self._name = str(name)
        if not isinstance(mode, str):
            raise TypeError("invalid mode: %r" % (mode,))
        mode = _validate_and_convert_mode(mode)
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newlines = newline
        self._close = closefd

        self._real_fd = None
        self._fd = None
        self._closed = False

        self._readbuffer = StringIO(u'')

    def flush(self):
        if self._fd:
            self._fd.flush()

    def fileno(self):
        return self._fd.fileno()

    def readable(self):
        return super().readable() or ('r' in self._mode or '+' in self

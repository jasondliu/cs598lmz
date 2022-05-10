import io
class File(io.RawIOBase):
    class _SharedFileHandle(object):
        __slots__ = ['_handle']
        def __init__(self, handle):
            self._handle = handle
        def close(self):
            self._handle = None
        def __int__(self):
            return self._handle
    def __init__(self, name, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self.__handle = None
        self._closed = False
        self._closefd = closefd
        self._mode = mode
        self._name = name
        self._readable = False
        self._seekable = False
        self._writable = False
        if self._mode:
            result = self._parse_mode_and_encoding(self._mode, encoding, errors)
            if result and self._mode in {'r', 'r+', 'w', 'w+', 'a', 'a+'}:
                self._mode, self._encoding, self._errors = result
                if self._mode

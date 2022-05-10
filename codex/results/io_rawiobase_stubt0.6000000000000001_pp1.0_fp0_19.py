import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        self._name = name
        self._mode = mode
        self._encoding = encoding
        self._errors = errors
        self._newline = newline
        self._closefd = closefd
        self._opener = opener
        self._fd = None
        self._file = None
        if 'b' in mode:
            if buffering < 0:
                buffering = io.DEFAULT_BUFFER_SIZE
            if buffering == 0:
                raise ValueError('can\'t have unbuffered text I/O')
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering < 1:
            raise ValueError('invalid buffering size')
        if newline is not None and 'b' in mode:
            raise ValueError('binary mode doesn\'t take a newline argument')
        if 'x' in mode and os.path.ex

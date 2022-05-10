import io
class File(io.RawIOBase):
    def __init__(self, name, mode, encoding=None, errors=None,
                 newline=None, line_buffering=False, **kwargs):
        self._closefd = False
        if isinstance(name, int):
            self._fd = name
            self._closefd = False
        else:
            self._fd = os.open(name, self._mode_to_flags(mode), 0o600)
            self._closefd = True
        if encoding is not None:
            if 'b' in mode:
                raise ValueError("Cannot specify both 'encoding' and 'b'.")
            if errors is None:
                errors = 'strict'
            if newline is None:
                newline = ''
            self._line_buffering = line_buffering
            self._encoding = encoding
            self._errors = errors
            self._write_stack = []
            self._read_stack = []
            self._read_encoding_stack = []
            self._read_translate_stack = []
            self._readuniversal = False
            self

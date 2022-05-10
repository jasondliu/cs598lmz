import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
        self._reading = 'r' in mode
        self._writing = 'w' in mode
        self._closed = False
        self._softspace = 0
        self._name = getattr(file, 'name', None)
        self._encoding = getattr(file, 'encoding', None)
        self._errors = getattr(file, 'errors', None)
        self._newlines = None
        self._line_buffering = False
        self._universal_newlines = False
        self._writable_file = None
        self._readable_file = None
        self._writable_file = self._file if self._writing else None
        self._readable_file = self._file if self._reading else None
        self._buffer = io.BytesIO()
        self._buffer_size = 0
        self._buffer_pos = 0
        self._buffer_end = 0
        self._buffer_view = memoryview(self._buffer.getbuffer())


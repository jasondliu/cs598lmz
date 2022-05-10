import io
class File(io.RawIOBase):
    def __init__(self, file_path: str, mode: str = 'r'):
        self._file = open(file_path, mode)
        self._mode = mode
        self._file_path = file_path
        self._file_size = os.path.getsize(file_path)
        self._file_pos = 0
        self._file_end = self._file_size
        self._file_start = 0
        self._file_eof = False
        self._file_closed = False
        self._file_read_pos = 0
        self._file_read_end = 0
        self._file_read_start = 0
        self._file_read_eof = False
        self._file_read_closed = False
        self._file_read_buffer = b''
        self._file_read_buffer_pos = 0
        self._file_read_buffer_end = 0
        self._file_read_buffer_start = 0
        self._file_read_buffer_eof = False
        self._file_read_buffer_closed

import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._file = None
        self._buffer = None
        self._buffer_size = 0
        self._buffer_pos = 0
        self._buffer_dirty = False
        self._buffer_eof = False
        self._buffer_eof_pos = 0
        self._buffer_eof_dirty = False
        self._buffer_eof_dirty_pos = 0
        self._buffer_eof_dirty_size = 0
        self._buffer_eof_dirty_data = None
        self._buffer_eof_dirty_data_pos = 0
        self._buffer_eof_dirty_data_size = 0
        self._buffer_eof_dirty_data_dirty = False
        self._buffer_eof_dirty_data_dirty_pos = 0
        self._buffer_eof_dirty_data_dirty_size = 0
        self._buffer_eof_dirty_data_dirty_data = None
        self._buffer_eof_dirty

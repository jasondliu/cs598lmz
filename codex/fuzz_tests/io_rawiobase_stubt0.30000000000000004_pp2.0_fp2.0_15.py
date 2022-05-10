import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True, opener=None):
        if opener is not None:
            raise NotImplementedError("opener not supported")
        self._closefd = closefd
        self._mode = mode
        self._name = name
        self._file = None
        self._file_id = None
        self._offset = 0
        self._size = 0
        self._buffer = None
        self._buffer_offset = 0
        self._buffer_size = 0
        self._buffer_dirty = False
        self._buffer_readonly = False
        self._buffer_max_size = 1024 * 1024
        self._buffer_read_size = 1024 * 1024
        self._buffer_write_size = 1024 * 1024
        self._buffer_write_count = 0
        self._buffer_read_count = 0
        self._buffer_write_count_max = 1024
        self._buffer_read_count_max = 1024
        self._buffer_write_size_max = 1024 * 1024 * 1024
        self._buffer_read_size

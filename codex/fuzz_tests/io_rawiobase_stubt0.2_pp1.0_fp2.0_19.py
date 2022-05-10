import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._file = open(filename, mode)
        self._mode = mode
        self._filename = filename
        self._offset = 0
        self._size = os.path.getsize(filename)
        self._buffer = b''
        self._buffer_offset = 0
        self._buffer_size = 0
        self._buffer_dirty = False
        self._buffer_dirty_offset = 0
        self._buffer_dirty_size = 0
        self._buffer_dirty_data = b''
        self._buffer_dirty_data_offset = 0
        self._buffer_dirty_data_size = 0
        self._buffer_dirty_data_size_max = 1024
        self._buffer_dirty_data_size_max_max = 1024 * 1024
        self._buffer_dirty_data_size_max_max_max = 1024 * 1024 * 1024
        self._buffer_dirty_data_size_max_max_max_max = 1024 * 1024 * 1024 * 1024
        self._buffer_dirty_data_size_max

import io
class File(io.RawIOBase):
    """
    A file-like object that can be used to
    access the contents of a file in memory.
    """
    def __init__(self, file_path, mode='rb'):
        """
        Constructor.
        :param file_path: The path to the file.
        :param mode: The mode in which to open the file.
        """
        if mode not in ('rb', 'wb', 'ab'):
            raise ValueError('Invalid mode: %s' % mode)
        self._mode = mode
        self._file_path = file_path
        self._size = os.path.getsize(file_path)
        self._buffer = b''
        self._buffer_offset = 0
        self._buffer_len = 0
        self._pos = 0
    
    def read(self, size=-1):
        """
        Reads size bytes from the file-like object.
        If size is -1, the entire file will be read.
        :param size: The number of bytes to read.
        :return: A byte string containing the bytes read.

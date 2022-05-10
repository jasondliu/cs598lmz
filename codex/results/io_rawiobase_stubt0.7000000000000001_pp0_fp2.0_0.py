import io
class File(io.RawIOBase):
    """
    A file-like object with the following features:
    - the file is read-only
    - the file has a known size
    - the file is a memory-mapped file (no RAM overhead)
    - the file is always opened in binary mode
    """
    def __init__(self, filename, mode='r'):
        super(File, self).__init__()

        self._filename = filename
        self._mode = 'r'
        self._size = os.stat(filename).st_size

        if sys.version_info[0] == 2:
            self._fd = open(filename, mode)
        else:
            self._fd = io.open(filename, mode)

        self._mm = mmap.mmap(self._fd.fileno(), self._size, access=mmap.ACCESS_READ)

    def read(self, size=-1):
        if size < 0:
            return self._mm[:]
        else:
            return self._mm[:size]

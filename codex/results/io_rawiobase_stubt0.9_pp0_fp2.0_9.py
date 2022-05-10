import io
class File(io.RawIOBase):
    """Raw I/O implementation for file objects on Windows."""

    '''
    Wrapper for Windows file objects.
    '''

    def __init__(self, handle):
        self._handle = handle

    def close(self):
        try:
            super().close()
        finally:
            CloseHandle(self._handle)

    def fileno(self):
        # Returns an invalid handle to avoid clashes with os.fdopen
        # wrapping an OS handle in a Python file object
        return -1

    # Measure the performance of reading and writing 32 or 64KB at a time.
    # Use the better one.
    blocksize = min(io.DEFAULT_BUFFER_SIZE, max(io.DEFAULT_BUFFER_SIZE, 2**15))
    del DEFAULT_BUFFER_SIZE

    def readinto(self, b):
        n = c_int(0)
        buffer = b[:blocksize]
        res = ReadFile(self._handle, buffer, len(buffer), byref(n), None)
        return n.value

    def write(self,

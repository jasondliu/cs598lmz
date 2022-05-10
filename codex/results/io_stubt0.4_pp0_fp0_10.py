import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# This test is only relevant on Windows.
if sys.platform == "win32":
    import _winapi
    # This test is only relevant when the file handle is not a socket.
    if not isinstance(_winapi.get_osfhandle(0), int):
        import _io
        # The file handle must be closed.
        assert view is None
        # The file handle must be closed only once.
        assert _io._IOBase__file_closed_count == 1

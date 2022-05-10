import io
class File(io.RawIOBase):
    def __init__(self, handle):
        self.handle = handle

    def fileno(self):
        return self.handle.fileno()

    def write(self, data):
        return self.handle.write(data)

    def readinto(self, b):
        return self.handle.readinto(b)

def file(handle):
    return File(handle)

def open(path, mode="r"):
    from _io import open
    return open(path, mode)

def _open_file(path, mode, buffering):
    return File(_open_osfhandle(path, mode, buffering))

import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self._name = name
        self._mode = mode
    def close():
        return 0

class FileDescriptor:
    def __init__(self, fd):
        self._fd = fd
    def close():
        return 0

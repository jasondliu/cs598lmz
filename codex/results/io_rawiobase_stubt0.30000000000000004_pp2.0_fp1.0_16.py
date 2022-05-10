import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        pass
    def fileno(self):
        return 0
    def close(self):
        pass
    def read(self, *args, **kwargs):
        return b''
    def readinto(self, *args, **kwargs):
        return 0
    def readline(self, *args, **kwargs):
        return b''
    def write(self, *args, **kwargs):
        return 0
    def seek(self, *args, **kwargs):
        pass
    def tell(self, *args, **kwargs):
        return 0
    def truncate(self, *args, **kwargs):
        pass
    def flush(self, *args, **kwargs):
        pass
    def readall(self, *args, **kwargs):
        return b''
    def readinto1(self, *args, **kwargs):
        return 0
    def readable(self, *args, **kwargs):
        return False
    def writable(self, *args,

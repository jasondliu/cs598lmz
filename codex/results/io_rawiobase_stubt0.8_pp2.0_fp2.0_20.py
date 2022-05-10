import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.filepath = filepath
        self.handle = None
    def open(self):
        if self.handle:
            raise Exception("File already open")
        mode, buffering = getattr(self, 'mode', 'rb'), getattr(self, 'buffering', -1)
        self.handle = open(self.filepath, mode, buffering)
        return self.handle
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    def __del__(self):
        self.close()
    def close(self):
        if self.handle:
            self.handle.close()
            self.handle = None
    def readable(self):
        return self.handle.readable()
    def writable(self):
        return self.handle.writable()
    def seekable(self):
        return self.handle.seekable()
    def readinto(self, b):

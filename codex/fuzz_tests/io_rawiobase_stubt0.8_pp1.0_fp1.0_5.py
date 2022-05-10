import io
class File(io.RawIOBase):
    def __init__(self):
        self.buffer = ""
    def write(self, b):
        self.buffer += b
    def read(self, b):
        data, self.buffer = self.buffer[:b], self.buffer[b:]
        return data
    @property
    def closed(self):
        return False
    def close(self):
        pass

stdout = File()
stderr = File()

__version__ = "0.1"

class tmp:
    class __Writer:
        def __init__(self, stream):
            self.stream = stream
            self.buffer = []
            self.size = 0
        def write(self, b):
            self.buffer.append(b)
            self.size += len(b)
        def flush(self):
            sys.__getattr__(self.stream).write("".join(self.buffer))
            self.buffer = []
            self.size = 0
        def close(self):
            pass
        def closed(self):
            return False
        def is

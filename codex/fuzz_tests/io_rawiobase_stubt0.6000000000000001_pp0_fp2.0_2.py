import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode
        self.fd = None
    def __enter__(self):
        self.fd = open(self.name, self.mode)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()
    def read(self, size=-1):
        return self.fd.read(size)
    def write(self, buffer):
        return self.fd.write(buffer)
    def flush(self):
        return self.fd.flush()
    def close(self):
        return self.fd.close()
file_obj = File("hello.txt", "w")
with file_obj as f:
    f.write("hello")

class File(object):
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode
        self.fd = None
    def __enter__(self):
        self

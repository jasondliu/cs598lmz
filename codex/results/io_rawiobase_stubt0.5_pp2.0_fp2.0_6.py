import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None

    def open(self):
        if self.fd is not None:
            raise ValueError("File is already open")
        self.fd = open(self.name, "rb")

    def close(self):
        if self.fd is None:
            raise ValueError("File is not open")
        self.fd.close()
        self.fd = None

    def readinto(self, b):
        if self.fd is None:
            raise ValueError("File is not open")
        return self.fd.readinto(b)

    def readable(self):
        return True

    def writable(self):
        return False

f = File("/tmp/foo")
f.open()
f.close()
f.readable()
f.writable()

f.readinto(b"")
f.write(b"")

class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
       

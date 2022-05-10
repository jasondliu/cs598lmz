import io
class File(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def close(self):
        pass

def open(name, mode="r", buffering=0):
    return File()

def close(f):
    pass

def read(f, size=1):
    return os.read(f, size)

def write(f, data):
    return os.write(f, data)

def seek(f, where, whence=0):
    return os.seek(f, where, whence)

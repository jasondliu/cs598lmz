import io
class File(io.RawIOBase): # compat with io.FileIO
    def __init__(self, file, *args, **kwargs):
        self.f = pymicmac.file.File(file)

    def __del__(self):
        self.f.close()

    def close(self):
        self.f.close()
        return super().close()

    def read(self, size=-1):
        return self.f.read(size)

    def write(self, data):
        self.f.write(data)

    def tell(self):
        return self.f.tell()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def open(file, mode):
    if 'b' not in mode:
        raise ValueError("only mode 'rb' is currently supported")
    return File(file)

# load C++ bindings

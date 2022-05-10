import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self.filename = filename
        self.mode = mode
        self.fd = None

    def open(self):
        self.fd = os.open(self.filename, self.mode)

    def __fspath__(self):
        return self.filename
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fileno(self):
        return self.fd

with File(filename, mode) as fd:
    print(fd)

print(fd)

# class File(io.RawIOBase):
#     def __init__(self, filename, mode='rb'):
#         self.filename = filename
#         self.mode = mode
#         self.fd = None

#    

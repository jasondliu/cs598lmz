import io
class File(io.RawIOBase):
    def __init__(self):
        self.fd = 3
    def fileno(self):
        return self.fd

a = File()
m = mmap.mmap(a.fileno(), 1024)
print(m)

import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self.fd = open(filename, mode)
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
    def fileno(self):
        return self.fd.fileno()
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return False
    def readinto(self, b):
        return self.fd.readinto(b)
    def seek(self, offset, whence=0):
        return self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
import io
f = File('/tmp/test.bin')
print(f.read(4))
f.seek(1)
print(f.read(4))

f.close()

print(f.closed)
 
# f.read(4)

# f = open('/tmp/test.bin', '

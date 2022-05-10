import io
# Test io.RawIOBase?
class T(io.RawIOBase):
    def __init__(self):
        pass
    def write(self, x):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def seek(self, x, y=0):
        pass
    def tell(self):
        pass
    def readinto(self, x):
        pass
    def close(self):
        pass
t = T()
print(t)

try:
    t = T()
    t.close()
    t.close()
except ValueError:
    print('ValueError')

try:
    t = T()
    t.close()
    t.write(b'123')
except ValueError:
    print('ValueError')
try:
    t = T()
    t.close()
    t.readable()
except ValueError:
    print('ValueError')

try:
    t = T()
    t.close()
    t.write

import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.handle = open(name, mode)
        self.readable = 'r' in mode
        self.writable = 'w' in mode
    def read(self, size=-1):
        return self.handle.read(size)
    def write(self, data):
        return self.handle.write(data)
    def close(self):
        return self.handle.close()

f = File('/etc/passwd')
f.readable
f.writable
f.read()
f.write(b'abc')
f.close()
# f.read()

# io.TextIOWrapper

import io
class File(io.TextIOWrapper):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.handle = open(name, mode)
        self.readable = 'r' in mode
        self.writable = '

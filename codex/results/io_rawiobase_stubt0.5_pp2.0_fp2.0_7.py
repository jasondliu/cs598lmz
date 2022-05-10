import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode

    def read(self, n=-1):
        with open(self.name, 'r') as f:
            return f.read()

    def readinto(self, b):
        with open(self.name, 'r') as f:
            data = f.read()
        b[:len(data)] = data
        return len(data)

    def write(self, b):
        with open(self.name, 'w') as f:
            f.write(b)
        return len(b)

class StringIO(io.RawIOBase):
    def __init__(self, initial_value=''):
        self.buf = initial_value

    def read(self, n=-1):
        if n == -1:
            ret = self.buf
            self.buf = ''
            return ret
        else:
            ret = self.buf[:n]
            self.buf = self.buf[n:]
            return

import io
class File(io.RawIOBase):
    def read(self, n=-1):
        if n >= 0:
            if n > len(self.buffer):
                n = len(self.buffer)
            retval = self.buffer[:n]
            self.buffer = self.buffer[n:]
            return retval
        return self.buffer
    def write(self, s):
        self.buffer += s
    def seek(self, n, mode=0):
        raise NotImplementedError
    def tell(self):
        raise NotImplementedError

f = File()
f.write('hello')
print(f.read(2))

print(f.read())

f.write('world')
print(f.read())

print(f.buffer)

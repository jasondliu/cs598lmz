import io
class File(io.RawIOBase):
    def __init__(self, f, buffer_size=io.DEFAULT_BUFFER_SIZE):
        self.f = f
        self.buffer_size = buffer_size
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b) # b is usually bytearray
        c = memoryview(b).cast('B')
        try:
            while n > 0:
                buf = self.f.read(min(n, self.buffer_size))
                if not buf:
                    break
                c[:len(buf)] = buf
                n -= len(buf)
        finally:
            if n > 0:
                c[:-n] = b'' # zero the end if we didn't use it all
        return len(b) - n
file = File(open('../../data/python-logo.png', 'rb'))
 
# with open('../../data/python-logo.png', 'rb') as f:
with file as f:
    # b = f.read()
   

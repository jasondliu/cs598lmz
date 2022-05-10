import io
class File(io.RawIOBase):
    def __init__(self):
        self.buffer = io.BytesIO()
    def read(self, n=-1):
        return self.buffer.read(n)
    def write(self, b):
        self.buffer.write(b)
    def seek(self, n):
        self.buffer.seek(n)
    def tell(self):
        return self.buffer.tell()
    def close(self):
        self.buffer.close()

f = File()
f.write(b"abc")
f.seek(0)
f.read()
f.close()

f = File()
f.write(b"abc")
f.seek(0)
f.read()
f.close()

#
#
#
#
#

import io
class File(io.RawIOBase):
    def __init__(self):
        self.buffer = io.BytesIO()
    def read(self, n=-1):
        return self.buffer.read(n)
    def write(self, b):
        self.buffer

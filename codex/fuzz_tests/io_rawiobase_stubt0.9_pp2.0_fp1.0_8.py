import io
class File(io.RawIOBase):
    def __init__(self):
        self.data = ""
        super().__init__()

    def write(self, x):
        self.data += x

    def read(self, x):
        line = self.data[:x]
        self.data = self.data[x:]
        return line

    def readable(self):
        return True
    
    def writable(self):
        return True


f = File()
f.write(b"hello ")
f.write(b"world!")
f.read(3)
#'hel'
f.read(3)
#'lo '
f.read(3)
#'wor'
f.read(3)
#'ld!'
f.read(3)
#''

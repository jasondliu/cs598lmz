import io
# Test io.RawIOBase.readall
class RIO(io.RawIOBase):
    def readable(self):
        return True
    def readall(self):
        return b'42'

r = RIO()
print(r.readall())

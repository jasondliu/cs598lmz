import io
# Test io.RawIOBase.readall
class RIO(io.RawIOBase):
    def readable(self):
        return True
    def readall(self):
        return b'42'

r = RIO()
print(r.readall())
try:
    r.write(b'42')
except OSError:
    print("Error")
# Test io.TextIOBase.readall
class TIO(io.TextIOBase):
    def readable(self):
        return True
    def readall(self):
        return '42'

t = TIO()
print(t.readall())
try:
    t.write('42')
except OSError:
    print("Error")

import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'

r = RawI()
print(r.read(1))
print(r.read(2))
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())
print(r.read())

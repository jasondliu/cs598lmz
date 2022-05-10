import io
# Test io.RawIOBase.
# Test io.RawIOBase.readinto


class ZeroRaw(io.RawIOBase):

    def readinto(self, b):
        for i in range(len(b)):
            b[i] = 0


for i in range(15):
    c = ZeroRaw()
    b = bytearray(i)
    l = c.readinto(b)
    if l != i:
        print('readinto should return len(b), returned', l)
        break
    for j in b:
        if j != 0:
            print('wrong content in b', j)
            break

# Test io.RawIOBase.readall
class OneRaw(io.RawIOBase):

    def readall(self):
        return b'1'


for s in [b'', b'a', b'hello']:
    c = OneRaw()
    a = c.readall()
    if a != b'1':
        print('readall returned wrong content', a)
        break
    if c.read(1) or c.read

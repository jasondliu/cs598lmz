import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        for i in range(len(b)):
            b[i] = (i+1) & 0xff
        return len(b)

    def readable(self):
        return True

def test():
    import array
    b = bytearray(b'\x00' * 100)
    m = MyRawIO()
    a = array.array('b', b'\x00' * 100)
    n = m.readinto(b)
    m.readinto(a)
    print(b[:10])
    print(b[-10:])
    print(n)
    print(a[:10])
    print(a[-10:])
    print(m.readinto(b) == 0)
    print(m.readinto(a) == 0)

test()

from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4

def unpack(fmt, f):
    return s.unpack(f.read(s.size))[0]

def pack(fmt, f, val):
    f.write(s.pack(val))

def load(f):
    return unpack('>I', f)

def save(f, val):
    pack('>I', f, val)

def test():
    import io
    f = io.BytesIO()
    save(f, 0x12345678)
    f.seek(0)
    assert load(f) == 0x12345678

if __name__ == '__main__':
    test()

import _struct
# Test _struct.Struct

def test_struct(fmt):
    s = _struct.Struct(fmt)
    size = s.size
    print(fmt, size)
    pack = s.pack
    unpack = s.unpack
    for i in range(10):
        x = random.randrange(256)
        y = random.randrange(256)
        z = random.randrange(256)
        w = random.randrange(256)
        data = pack(x, y, z, w)
        print(x, y, z, w, data)
        assert len(data) == size
        x, y, z, w = unpack(data)
        print(x, y, z, w)
        assert (x, y, z, w) == (x&255, y&255, z&255, w&255)

def test_struct_format(fmt):
    s = _struct.Struct(fmt)
    size = s.size
    print(fmt, size)
    pack = s.pack
    unpack = s.un

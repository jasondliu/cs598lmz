from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')

def pack(fmt, *args):
    return s.pack(fmt, *args)

def unpack(fmt, *args):
    return s.unpack(fmt, *args)

def calcsize(fmt):
    return s.calcsize(fmt)

# ____________________________________________________________

def test_struct():
    assert pack('h', -1) == '\xff\xff'
    assert pack('h', 0) == '\x00\x00'
    assert pack('h', 1) == '\x00\x01'
    assert pack('h', -2) == '\xfe\xff'
    assert pack('h', 2) == '\x00\x02'
    assert pack('h', -3) == '\xfd\xff'
    assert pack('h', 3) == '\x00\x03'
    assert pack('h', -4) == '\xfc\xff'

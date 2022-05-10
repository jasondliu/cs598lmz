from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def test():
    assert unpack(pack(0)) == 0
    assert unpack(pack(1)) == 1
    assert unpack(pack(2**31-1)) == 2**31-1
    assert unpack(pack(-1)) == -1
    assert unpack(pack(-2**31)) == -2**31
    assert unpack(pack(2**31)) == -2**31
    assert unpack(pack(-2**31-1)) == -2**31-1
    assert unpack(pack(2**31+1)) == -2**31+1
    assert unpack(pack(2**32-1)) == -1
    assert unpack(pack(-2**32)) == 0
    assert unpack(pack(2**32)) == 0
    assert unpack(pack(-2**32+1)) == 1

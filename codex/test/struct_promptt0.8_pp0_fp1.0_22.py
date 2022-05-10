import _struct
# Test _struct.Struct object
St = _struct.Struct("i")
St.size
St.pack(1)
St.pack_into(b"", 0, 1)
St.unpack(St.pack(1))
St.unpack_from(St.pack(1), 0)
# Test _struct module
_struct.calcsize("i")
_struct.pack("i", 1)
_struct.pack_into(b"", 0, "i", 1)
_struct.unpack("i", _struct.pack("i", 1))
_struct.unpack_from("i", _struct.pack("i", 1), 0)

class St(object):
    def __repr__(self):
        return "St()"
class SubSt(St):
    def __repr__(self):
        return "SubSt()"
_struct.Struct("i").pack(St())
_struct.Struct("i").pack(SubSt())
_struct.Struct("i").pack(1)

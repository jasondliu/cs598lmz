from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack = Struct.__dict__['pack']
s.unpack = Struct.__dict__['unpack']

def _pack(v):
    return s.pack(v)
def _unpack(v):
    return s.unpack(v)[0]

def _pack_array(a):
    return "".join(map(_pack, a))
def _unpack_array(a):
    return map(_unpack, a)

def _pack_array_n(a):
    return "".join(map(_pack, a))
def _unpack_array_n(a):
    return map(_unpack, a)

def _pack_array_nn(a):
    return "".join(map(_pack_array_n, a))

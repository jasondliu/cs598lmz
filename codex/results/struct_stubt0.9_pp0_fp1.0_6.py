from _struct import Struct
s = Struct.__new__(Struct)
s.pack = lambda x: _enum
s.pack_into = lambda x, y, z: _enum
s.unpack_from = lambda x, y: _enum
s.unpack = lambda x: _enum
s.size = _enum = Enum([
  'calcsize',
  'pack_into',
  'unpack_from',
  'unpack'])
_enum = None
#</definitions>#

#<header>#
setattr(Struct, "__module__", "ctypes")
#</header>#

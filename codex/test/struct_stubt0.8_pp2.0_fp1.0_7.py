from _struct import Struct
s = Struct.__new__(Struct)
def _pack(self, format, v1, v2):
  return struct.pack(format, v1, v2)
s.pack = _pack

def _unpack(self, format, string):
  return struct.unpack(format, string)
s.unpack = _unpack

def _calcsize(self, format):
  return struct.calcsize(format)
s.calcsize = _calcsize

Struct.pack = _pack
Struct.unpack = _unpack
Struct.calcsize = _calcsize

def _pack_into(self, format, buf, offset, v1, v2):
  struct.pack_into(format, buf, offset, v1, v2)
Struct.pack_into = _pack_into

def _unpack_from(self, format, buf, offset=0):
  return struct.unpack_from(format, buf, offset)
Struct.unpack_from = _unpack_from


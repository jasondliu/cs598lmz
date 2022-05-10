from _struct import Struct
s = Struct.__new__(Struct)
s.formatstring = '<2h'
s.size = 4


def unpack(f):
  return s.unpack(f.read(s.size))


def size(props):
  return s.size


def pack(props):
  return s.pack(*props)

from _struct import Struct
s = Struct.__new__(Struct)

s.format = '<2sb2si2d2fpI'
s.size = s.calcsize()
s.pattern = b'@\x13\x00\x00\x00\x00\x00\x00d\xfb@@\x00\x00@\x00\x00@\xd0\x00\x00\x00\x00\x00\x00p\xdf@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

#
# The following codes look redundant but are needed for PyPy
#

if sys.byteorder == 'little':
  s.pack
  s.unpack
  s.unpack_from
  s.iter_unpack

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', bytearray(b'\x01\x00\x00\x00\x02\x00\x03\x00'), 0)
s.format_str = 'hhl'
s.size = struct.calcsize(s.format_str)
s.unpack_from(bytearray(b'\x01\x00\x00\x00\x02\x00\x03\x00'), 0)

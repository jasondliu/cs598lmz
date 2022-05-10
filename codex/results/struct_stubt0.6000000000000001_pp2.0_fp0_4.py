from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
s.unpack('\x00')[0]

s = Struct.__new__(Struct)
s.format = 'b'
s.size = 1
s.unpack('\x00')[0]

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
s.unpack('\x00')[0]

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
s.unpack('\xff')[0]

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
s.unpack('\x7f')[0]

s = Struct.__new__(Struct)
s.format = 'b'
s.size = 1
s.unpack('\xff')[0]

s = Struct.__new__(Struct)
s.format = 'b'
s.size = 1
s.unpack('\x

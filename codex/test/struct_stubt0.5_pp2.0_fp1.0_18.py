from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>L')
s.size

s.pack(12345)

s.unpack(_)

s.unpack(_[:s.size])

s.unpack(_[0:s.size])

s.unpack(_[0:])

s.unpack(_[:-1])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])

s.unpack(_[-s.size:])


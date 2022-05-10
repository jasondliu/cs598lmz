from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<b'
s.size = len(s.pack(0))
s.format += s.format
s.size += s.size
s.unpack(s.pack(0, 0))
s.unpack(s.pack(0, 0))
s.unpack(s.pack(*(0, 0)))
s.unpack(s.pack(0, 0, 0))

# test bug https://bugs.python.org/issue16334
self = Struct.__new__(Struct)
self.format = '<b'
self.size = len(self.pack(0))
self.format += self.format
self.size += self.size
self.unpack(self.pack(0, 0))
self.unpack(self.pack(0, 0))
self.unpack(self.pack(*(0, 0)))
self.unpack(self.pack(0, 0, 0))

s = Struct.__new__(Struct)
s.format = '<b'

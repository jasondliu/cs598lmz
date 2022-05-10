from _struct import Struct
s = Struct.__new__(Struct)

s.size = lambda: 5

# TypeError: 'Struct' object is not callable
s.pack(1)

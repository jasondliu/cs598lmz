from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&lt;I')
print(s.pack(50))

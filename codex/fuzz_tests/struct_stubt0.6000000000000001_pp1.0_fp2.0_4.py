from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('HH', b)
print(s.unpack(b))
</code>


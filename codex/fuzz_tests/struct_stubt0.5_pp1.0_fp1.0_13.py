from _struct import Struct
s = Struct.__new__(Struct)

s.format = 'i'
s.size = calcsize(s.format)

s.pack(1)
</code>


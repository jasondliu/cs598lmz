from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = struct.calcsize(s.format)
print("s.format = %r, s.size = %r" % (s.format, s.size))
#s.format = 'I', s.size = 4
</code>


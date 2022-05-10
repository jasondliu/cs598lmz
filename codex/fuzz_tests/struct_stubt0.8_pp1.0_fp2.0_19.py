from _struct import Struct
s = Struct.__new__(Struct)
fmt = 'hhl'
s.__init__(fmt)
buf = 'foo'
print s.unpack(buf)
</code>


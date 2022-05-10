from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>IIII'
s.size = len(data)
values = s.unpack(data)
print 'values:', values
print

# The fields method is a class method, so we have to use the class name
import struct
print 'fields:', struct.Struct.fields(s)
print

# Get the x field
x = Struct.__getitem__(s, 'x')
print x,len(x),struct.calcsize(x)
print

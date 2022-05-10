from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__ = Struct.__dict__
s

%timeit _struct.calcsize(s.format)
%timeit _struct.pack(s.format, *s)
%timeit _struct.unpack(s.format, b)
 
 
 
 
 
%timeit s.size
%timeit s.pack(*s)
%timeit s.unpack(b)

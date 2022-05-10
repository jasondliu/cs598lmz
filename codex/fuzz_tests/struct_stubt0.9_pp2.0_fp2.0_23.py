from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', True)
s.size

s = Struct('i', True)
s

s.size
s = Struct('i')
s
help(Struct)
s = Struct('ii')
s
 
s.size
import numpy as np
np.array([1, 2, 3], dtype='i').tobytes()
np.array([1, 2, 3], dtype='i2').tobytes()
s = Struct('i2')
s.size
s.pack(1)
s.pack(256)
s.pack(257)
s.pack(257, 258)
s = Struct('i2')
s.unpack(b'\x01\x00')
s = Struct('<i2')
s.unpack(b'\x01\x00')
s = Struct('>i2')
s.unpack(b'\x01\x00')
s = Struct('iI')
s = Struct('Ii')
s.size
s = Struct('i')
s.pack(1)

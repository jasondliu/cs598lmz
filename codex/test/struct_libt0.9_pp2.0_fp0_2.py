import _struct

_a = numpy.arange(10)
_a *= 1.0/numpy.max(_a) # normalize
_a.shape = (2, 5)

data = (ctypes.c_char*_a.size).from_buffer(_a) # byte array 

_a.shape = (2, 5)
shape = (ctypes.c_int*_a.ndim)(*_a.shape) # row, col

fd = open("test.struct", "wb+")

fd.write(_struct.pack("P"*3, 
                      ctypes.addressof(data), 
                      ctypes.addressof(shape), 
                      ctypes.c_ulong(int(_a.dtype.char))))

#fd.seek(0, os.SEEK_SET)

_b = ctypes.cast(ctypes.addressof(data),
                 ctypes.POINTER(ctypes.c_inf))

fd2 = open("test.dat", "wb+")

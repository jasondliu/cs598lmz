import ctypes
# Test ctypes.CField()
assert ctypes.CField(ctypes.c_char, 'mybyte') == 'mybyte : char ;'
assert ctypes.CField(ctypes.c_byte, 'mybyte') == 'mybyte : byte ;'
assert ctypes.CField(ctypes.c_ubyte, 'myubyte') == 'myubyte : ubyte ;'
assert ctypes.CField(ctypes.c_int, 'myint') == 'myint : int ;'
assert ctypes.CField(ctypes.c_longlong, 'mylonglong') == 'mylonglong : long ;'
assert ctypes.CField(ctypes.c_size_t, 'mysize_t') == 'mysize_t : ulong ;'
assert ctypes.CField(ctypes.c_float, 'myfloat') == 'myfloat : single ;'
assert ctypes.CField(ctypes.c_double, 'mydouble') == 'mydouble : double ;'
assert ctypes.CField(ctypes.c_longdouble, 'mylongdouble') ==

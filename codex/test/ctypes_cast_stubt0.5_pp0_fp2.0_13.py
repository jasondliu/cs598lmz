import ctypes
ctypes.cast(1, ctypes.c_void_p)

#<codecell>

ctypes.cast(1, ctypes.c_void_p).value

#<codecell>

ctypes.c_void_p(1)

#<codecell>

ctypes.c_void_p(1).value

#<codecell>

ctypes.cast(1, ctypes.c_void_p) == ctypes.c_void_p(1)

#<codecell>

ctypes.cast(1, ctypes.c_void_p) == ctypes.c_void_p(0)

#<codecell>

ctypes.cast(1, ctypes.c_void_p).value == ctypes.c_void_p(0).value

#<codecell>

ctypes.c_void_p(1).value == ctypes.c_void_p(0).value

#<codecell>

ctypes.c_void_p(1).value == ctypes.c_void_p

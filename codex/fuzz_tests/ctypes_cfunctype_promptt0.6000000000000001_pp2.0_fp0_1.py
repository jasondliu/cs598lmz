import ctypes
# Test ctypes.CFUNCTYPE()

# http://stackoverflow.com/questions/9735084/how-to-call-a-c-function-from-python
# http://docs.python.org/2/library/ctypes.html

# void (*pf)(int);

# C compatible void(*)(int)
pf = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)

# Python compatible void(*)(int)
pf = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)

# C compatible void(*)(int)
pf = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)

# Python compatible void(*)(int)
pf = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)

# C compatible void(*)(int)
pf = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)

# Python compatible void(*

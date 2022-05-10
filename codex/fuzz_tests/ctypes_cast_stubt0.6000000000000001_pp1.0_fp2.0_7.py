import ctypes
ctypes.cast(p, ctypes.c_void_p).value

# 4.20
# import ctypes
# ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
# ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
# ctypes.pythonapi.PyCObject_AsVoidPtr(p)

# 4.21
# import socket
# socket.socket(socket.AF_INET, socket.SOCK_STREAM).fileno()

# 4.22
# import os
# os.fdopen(fd)

# 4.23
# import os
# os.open(filename, os.O_WRONLY|os.O_CREAT|os.O_TRUNC)

# 4.24
# import os
# os.fdopen(os.open(filename, os.O_WRONLY|os.O_CREAT|os.O_TRUNC))

# 4.25
# import os
# os.mkfifo

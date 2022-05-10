import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Users\Mateusz\AppData\Local\Programs\Python\Python37-32\lib\ctypes\__init__.py", line 125, in __call__
#     return self.callable(*args)
# TypeError: 'int' object is not callable

# OK
CFUNCTYPE_INT_INT = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CFUNCTYPE_INT_INT(lambda x: x)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Users\Mateusz\AppData\

import ctypes
ctypes.cast(0, ctypes.py_object)
 
# prints "<class 'ctypes.py_object'>"
print(ctypes.cast(0, ctypes.py_object).__class__)
 

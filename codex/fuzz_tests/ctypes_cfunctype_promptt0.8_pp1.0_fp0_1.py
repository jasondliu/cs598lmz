import ctypes
# Test ctypes.CFUNCTYPE when the function takes an array
# of pointers to a pointer
#
f2 = ctypes.CFUNCTYPE(None,ctypes.c_int,ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))(lambda a,b: print(a,b))
#>>> f2(1,[ctypes.pointer(c_double(1.0))])
#1 _ctypes.PyCPointerType(<class 'ctypes.c_double'>)

import _ctypes
#>>> dir(_ctypes.PyCPointerType)
#['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__getitem__', '_
#_name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_type_', 'from_param', 'in_dll', 'in_dll_


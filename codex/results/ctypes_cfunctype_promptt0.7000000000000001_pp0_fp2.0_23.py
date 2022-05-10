import ctypes
# Test ctypes.CFUNCTYPE function signature of a function that returns a C++ object.

def function():
    # Implicitly cast of a Python object to an object with a custom 
    # destructor should trigger the destructor.
    return (1, 2, 3)

# The number of arguments is 2: the return address and the object to destruct.
# There is no return type.
destructor = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.py_object)(function)

# The pointer to the destructor gets stored in the object's tp_del slot.
class MyObject(object):
    __slots__ = [ 'destructor' ]

obj = MyObject()
obj.destructor = destructor

# The __del__ slot is only invoked when the object is explicitly destroyed.
# This is different from the __del__ method, which is invoked when the object
# is about to be destroyed.
obj.__del__ = function

# The destructor is invoked when the object is destroyed.
del obj

# The __del__ method is invoked when the object is

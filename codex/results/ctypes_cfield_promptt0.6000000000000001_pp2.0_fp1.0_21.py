import ctypes
# Test ctypes.CField is a subclass of ctypes.CFuncPtr.
class X(ctypes.CField):
    pass

class Y(ctypes.CFuncPtr):
    pass

isinstance(X, Y)
# Test that ctypes.CField is a subclass of ctypes.CFuncPtr.
class X(ctypes.CField):
    pass

class Y(ctypes.CFuncPtr):
    pass

issubclass(X, Y)
# Test that ctypes.CField is a subclass of ctypes.CFuncPtr.
class X(ctypes.CField):
    pass

class Y(ctypes.CFuncPtr):
    pass

issubclass(ctypes.CField, ctypes.CFuncPtr)
# Test that ctypes.CField is a subclass of ctypes.CFuncPtr.
class X(ctypes.CField):
    pass

class Y(ctypes.CFuncPtr):
    pass

issubclass(ctypes.CField, ctypes.CFuncPtr)

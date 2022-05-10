import ctypes
# Test ctypes.CFUNCTYPE
subtype = ctypes.CFUNCTYPE(ctypes.py_object)
subtype.__bases__[0] is ctypes.CFUNCTYPE
subtype(lambda: None)
subtype(lambda x: x)
subtype(lambda x, y: x + y)
subtype(lambda *args: args)
subtype(lambda **kwargs: kwargs)
subtype(lambda *args, **kwargs: args)
subtype(lambda *args, **kwargs: kwargs)
subtype(lambda *args, **kwargs: (args, kwargs))
subtype(lambda *args, **kwargs: (args, kwargs))

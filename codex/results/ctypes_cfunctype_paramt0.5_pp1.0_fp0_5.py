import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class CppClass:
    def __init__(self, _lib, _cls, _cls_name):
        self.lib = _lib
        self.cls = _cls
        self.cls_name = _cls_name
        self.cls_ptr = None
        self.methods = {}

    def __getattr__(self, name):
        if name not in self.methods:
            # create method
            func = getattr(self.lib, self.cls_name + "_" + name)
            func.argtypes = [ctypes.c_void_p]
            func.restype = ctypes.c_void_p
            self.methods[name] = func
        return self.methods[name]

    def __call__(self, *args):
        # create object
        self.cls_ptr = self.cls(*args)
        return self

class Cpp:
    def __init__(self, lib_

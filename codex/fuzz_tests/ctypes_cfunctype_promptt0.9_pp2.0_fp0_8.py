import ctypes
# Test ctypes.CFUNCTYPE
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def PythonCall(x):
    return x

fptr = functype(PythonCall)
print fptr(2.0)

# Test subclassing
class FunctionPrototype(ctypes.CFUNCTYPE):
    def New(self, *args):
        return ctypes.CFUNCTYPE.__new__(self, *args)
    def __call__(self, *args):
        return ctypes.CFUNCTYPE.__call__(self, *args)

subclass = FunctionPrototype(None,    ctypes.c_double)
subclass = FunctionPrototype(subclass, ctypes.c_double)
subclass = FunctionPrototype(subclass, ctypes.c_double)
subclass = FunctionPrototype(subclass, ctypes.c_double)
subcla

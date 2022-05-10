import types
# Test types.FunctionType
ctypes.CFuncPtr(types.FunctionType)
try:
    ctypes.CFuncPtr(types.ClassType)
except TypeError: pass
else: raise Exception("ctypes.CFuncPtr(types.ClassType) didn't throw TypeError")
try:
    ctypes.CFuncPtr(types.ModuleType)
except TypeError: pass
else: raise Exception("ctypes.CFuncPtr(types.ModuleType) didn't throw TypeError")
try:
    ctypes.CFuncPtr(types.InstanceType)
except TypeError: pass
else: raise Exception("ctypes.CFuncPtr(types.InstanceType) didn't throw TypeError")
# Test types.StaticMethodType, types.ClassMethodType
class C(object):
    def m(self): pass
    m = staticmethod(m)
ctypes.CFuncPtr(type(C.m))
ctypes.CFuncPtr(type(C.m).__get__(10)(C()))
class C(object):
    def m(self): pass
    m = classmethod(m)
ctypes.

import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
cg = cython.compile(f)
assert not isinstance(cg, types.FunctionType)
# Test types.ModuleType
assert isinstance(cython, types.ModuleType)
assert not isinstance(cython.inline, types.ModuleType)
# Test types.MethodType
class A():
    @cython.cclass
    def m(self):
        pass
assert isinstance(A.m, types.MethodType)
assert not isinstance(cython.inline.inline, types.MethodType)
assert not isinstance(A.m, types.FunctionType)
# Test types.ClassType
class B():
    @cython.cclass
    def m(this):
        pass
assert isinstance(B, types.ClassType)
assert not isinstance(A, types.ClassType)
# Test types.TypeType
assert isinstance(A, types.TypeType)
assert not isinstance(object, types.TypeType)
# Test types.L

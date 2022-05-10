import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.FrameType
def f():
    import sys
    return sys._getframe()

assert isinstance(f(), types.FrameType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.SimpleNamespace
ns = types.SimpleNamespace(a=1)
assert ns.a == 1


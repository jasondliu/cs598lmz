import types
# Test types.FunctionType
def f():
    pass
assert(type(f) == types.FunctionType)
assert(type(f) == types.BuiltinFunctionType)

# Test types.GeneratorType
def g():
    yield 1
assert(type(g()) == types.GeneratorType)

# Test types.MethodType
class C:
    def m(self):
        pass
assert(type(C.m) == types.MethodType)
assert(type(C().m) == types.MethodType)

# Test types.ModuleType
assert(type(types) == types.ModuleType)
assert(type(os) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert(type(tb) == types.TracebackType)

# Test types.FrameType
def f():
    return sys._getframe()
assert(type(f()) == types.FrameType)

# Test types.CodeType
def f():
    pass
assert(type

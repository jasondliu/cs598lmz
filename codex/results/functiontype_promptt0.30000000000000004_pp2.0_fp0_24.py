import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C().m, types.MethodType)

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
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
assert isinstance(f(), types.FrameType)

# Test types.CodeType
def f

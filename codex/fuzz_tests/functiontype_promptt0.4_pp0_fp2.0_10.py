import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class C:
    def f(self): pass
    def g(self): pass

assert isinstance(C.f, types.BuiltinMethodType)
assert isinstance(C.g, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self): pass
    def g(self): pass

c = C()
assert isinstance(c.f, types.MethodType)
assert isinstance(c.g, types.MethodType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.TracebackType
try:
    raise IndexError
except IndexError:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    g()
def

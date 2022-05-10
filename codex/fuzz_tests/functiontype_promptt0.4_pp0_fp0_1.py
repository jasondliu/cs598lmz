import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.ClassType
class C: pass
assert type(C) == types.ClassType

# Test types.InstanceType
c = C()
assert type(c) == types.InstanceType

# Test types.MethodType
assert type(C.f) == types.MethodType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType

# Test types.CodeType
assert type(f.func_code) == types.CodeType

# Test types.TracebackType
try:
    raise Exception()
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) == types.FrameType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.DictProxyType
assert type(f.func_globals) == types.Dict

import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.ModuleType
assert type(types) is types.ModuleType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType

# Test types.NoneType
assert type(None) is types.NoneType

# Test types.NotImplementedType
assert NotImplemented is types.NotImplementedType

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.CodeType
# XXX: This should be uncommented when code objects are supported
#assert type(f.__code__) is types.CodeType

# Test types.FrameType
# XXX: This should be uncommented when frame objects are supported
#def f1():
#    return sys._getframe

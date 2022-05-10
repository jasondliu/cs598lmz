import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h(): yield 1
assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.FrameType
def i():
    assert type(sys._getframe()) == types.FrameType
i()

# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class C:
    def m(self): pass
assert

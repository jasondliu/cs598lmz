import types
# Test types.FunctionType
def f(): pass
print(type(f) == types.FunctionType)

# Test types.LambdaType
x = lambda: None
print(type(x) == types.LambdaType)

# Test types.GeneratorType
def g(): yield 1
print(type(g()) == types.GeneratorType)

# Test types.CodeType
def h(): pass
print(type(h.__code__) == types.CodeType)

# Test types.MappingProxyType
d = {1: 2}
print(type(types.MappingProxyType(d)) == types.MappingProxyType)

# Test types.SimpleNamespace
print(type(types.SimpleNamespace()) == types.SimpleNamespace)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    print(type(tb) == types.TracebackType)

# Test types.FrameType
def i():
    print(type(sys._getframe()) == types.FrameType

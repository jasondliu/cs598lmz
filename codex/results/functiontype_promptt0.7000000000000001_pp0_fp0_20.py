import types
# Test types.FunctionType
def test():
    pass

print type(test) == types.FunctionType

# Test types.LambdaType
print type((lambda: None)) == types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1

print type(gen()) == types.GeneratorType

# Test types.CodeType
print type(test.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    print type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
def some_function():
    return sys._getframe()

print type(some_function()) == types.FrameType

# Test types.BuiltinFunctionType
print type(min) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.TypeType
print type(test) == types.TypeType

# Test types.UnicodeType
print type(u

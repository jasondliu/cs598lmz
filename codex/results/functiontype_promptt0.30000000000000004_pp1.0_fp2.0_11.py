import types
# Test types.FunctionType
def foo(): pass

class A:
    def bar(self): pass

assert type(foo) is types.FunctionType
assert type(A.bar) is types.MethodType
assert type(A.bar.__func__) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

# Test types.CodeType
assert type(foo.__code__) is types.CodeType

# Test types.FrameType
def baz():
    return types.FrameType

assert type(baz()) is types.FrameType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb

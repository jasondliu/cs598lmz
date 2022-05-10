import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
# Test types.LambdaType
x = lambda: None
print(type(x) == types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1
g = gen()
print(type(g) == types.GeneratorType)

# Test types.CodeType
def foo(): pass
print(type(foo.__code__) == types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    print(type(sys.exc_info()[2]) == types.TracebackType)

# Test types.FrameType
def bar():
    import sys
    return sys._getframe()
print(type(bar()) == types.FrameType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class Foo(object):
    def __len__(self):
        pass
print(

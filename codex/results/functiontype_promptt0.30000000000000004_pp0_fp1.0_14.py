import types
# Test types.FunctionType
def foo():
    pass

class Foo(object):
    def bar(self):
        pass

assert isinstance(foo, types.FunctionType)
assert isinstance(Foo.bar, types.FunctionType)
assert isinstance(Foo.bar.__get__(Foo()), types.MethodType)

# Test types.LambdaType
f = lambda: None
assert isinstance(f, types.LambdaType)

# Test types.GeneratorType
def foo():
    yield 1

assert isinstance(foo(), types.GeneratorType)

# Test types.CodeType
def foo():
    pass

assert isinstance(foo.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def foo():
    return sys._getframe()

assert isinstance(foo(), types.FrameType)

#

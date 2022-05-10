import types
# Test types.FunctionType
def foo():
    pass
assert type(foo) is types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.MethodType
class Foo(object):
    def bar(self):
        pass
assert type(Foo.bar) is types.MethodType
# Test types.UnboundMethodType
assert type(Foo.bar.__get__(None, Foo)) is types.UnboundMethodType
# Test types.BuiltinMethodType
assert type(Foo.__new__) is types.BuiltinMethodType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
def foo():
    yield 1
assert type(foo()) is types.GeneratorType
# Test types.CodeType
assert type(foo.__code__) is types.CodeType
# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert type(sys.exc_info()[2]) is types.TracebackType

import types
# Test types.FunctionType
def foo(): pass
baz = foo
assert type(foo) is types.FunctionType
assert type(baz) is types.FunctionType
# Test types.MethodType
class A:
    def foo(self): pass
a = A()
assert type(A.foo) is types.MethodType
assert type(a.foo) is types.MethodType
# Test types.UnboundMethodType
class A:
    def foo(self): pass
assert type(A.foo) is types.MethodType
assert type(A.foo.__func__) is types.FunctionType
assert type(A.foo.__func__.__get__(42, A)) is types.MethodType
assert type(A.foo.__func__.__get__(42, A).__self__) is int
assert type(A.foo.__func__.__get__(None, A)) is types.UnboundMethodType
assert type(A.foo.__func__.__get__(None, A).__self__) is type
# Test types.BuiltinFunctionType
assert type(len) is types

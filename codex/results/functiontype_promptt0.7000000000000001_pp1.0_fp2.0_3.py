import types
# Test types.FunctionType

def foo():
    pass

assert type(foo) is types.FunctionType
assert type(lambda x: x) is types.LambdaType
assert type(foo.__call__) is types.MethodType
assert type(foo.__code__) is types.CodeType
assert type(foo.__code__.co_code) is bytes
assert type(foo.__closure__) is tuple
assert type(foo.__closure__[0]) is types.CellType
assert type(foo.__defaults__) is tuple
assert type(foo.__globals__) is dict
assert type(foo.__kwdefaults__) is dict
assert type(foo.__dict__) is types.MemberDesriptorType  # not exactly correct, but close
assert type(foo.__annotations__) is dict

class Foo:
    def bar(self):
        pass

assert type(Foo.bar) is types.MethodType
assert type(Foo.bar.__func__) is types.FunctionType
assert type(Foo.bar.__self__) is Foo


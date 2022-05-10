import types
# Test types.FunctionType for issue #10156

class Foo(object):
    def __new__(cls):
        return cls

Foo.__call__ = types.MethodType(lambda self: 42, None, Foo)
f = Foo()
print f()

Foo.__call__ = types.FunctionType(Foo.__call__.__func__.func_code, {},
                                  "__call__", None, None)
print f()

def bar():
    pass

print bar()

try:
    bar.__call__ = types.FunctionType(bar.__func__.func_code, {},
                                      "__call__", None, None)
    print bar()
except TypeError:
    # This must raise TypeError since 'bar' is not a class.
    pass

def baz():
    return baz.__call__()

baz.__call__ = types.FunctionType(baz.__func__.func_code, {},
                                  "__call__", None, None)
print baz()

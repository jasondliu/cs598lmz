from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))
list(FunctionType(lambda: None, globals(), 'foo', (1, 2, 3)))
list(FunctionType(lambda: None, globals(), 'foo', (), {'a': 1, 'b': 2}))
list(FunctionType(lambda: None, globals(), 'foo', (), {'a': 1, 'b': 2}, True))
list(FunctionType(lambda: None, globals(), 'foo', (), {'a': 1, 'b': 2}, True, True))

# __qualname__
def foo():
    pass

foo.__qualname__

# __self__
class Foo:
    def foo(self):
        pass

Foo.foo.__self__

# __code__
def foo():
    pass

foo.__code__

# __defaults__
def foo(a, b=1, c=2):
    pass

foo.__defaults__

# __kwdefaults__
def foo(a, b=1, c=2, *, d=

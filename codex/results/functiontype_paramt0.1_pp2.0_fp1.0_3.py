from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the repr of a function is correct
def foo():
    pass

foo.__name__ = 'bar'
foo.__qualname__ = 'baz'
foo.__module__ = 'qux'
foo.__defaults__ = (1, 2, 3)
foo.__kwdefaults__ = {'a': 1, 'b': 2, 'c': 3}
foo.__annotations__ = {'x': 1, 'y': 2, 'z': 3}
foo.__closure__ = (1, 2, 3)
foo.__code__ = 'code'
foo.__dict__ = {'a': 1, 'b': 2, 'c': 3}
foo.__doc__ = 'doc'
foo.__globals__ = globals()
foo.__text_signature__ = '(a, b, c)'

repr(foo)

# Test that the repr of a method is correct
class Foo:
    def bar(self):
        pass

Foo.bar.__

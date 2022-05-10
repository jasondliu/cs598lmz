from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the repr of a function is correct
def f():
    pass

f.__name__ = 'foo'
f.__qualname__ = 'bar'
f.__module__ = 'baz'
f.__defaults__ = (1, 2, 3)
f.__kwdefaults__ = {'a': 1, 'b': 2}
f.__annotations__ = {'c': 3, 'd': 4}
f.__closure__ = (1, 2, 3)
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
f.__globals__ = {'e': 5, 'f': 6}

assert repr(f) == "baz.bar(1, 2, 3, *, a=1, b=2, **kwargs)"

# Test that the repr of a method is correct
class C:
    def f(self):
        pass

C.f.

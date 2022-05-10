fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Generators are also objects (see test_types.py for more about this)
def f():
    yield 1
    yield 2
f.__code__ = 42
f.__code__
f.__code__ = f.__code__
f.__code__

# Test generator function attributes
def f():
    yield 1
    yield 2
f.__name__
f.__qualname__
f.__annotations__
f.__kwdefaults__
f.__defaults__
f.__code__
f.__closure__
f.__globals__
f.__dict__
f.__doc__
f.__module__
f.__defaults__ = (1, 2, 3)
f.__defaults__
f.__kwdefaults__ = {'a': 1, 'b': 2}
f.__kwdefaults__
f.__closure__ = (lambda: None, lambda: None)
f.__closure__
f.__annotations__ = {'a': 1, 'b': 2}
f.

import types
# Test types.FunctionType
#
# Example:
#   >>> foo = types.FunctionType(lambda x: x, globals(), 'foo', (), ('x',), None, None, None)
#   >>> foo(123)
#   123
#   >>> foo.__name__
#   'foo'
#   >>> foo.__code__.co_varnames
#   ('x',)
#   >>> foo.__closure__
#   None
#   >>> foo.__defaults__
#   None

def test(foo):
    print(foo.__name__)
    print(foo.__code__.co_varnames)
    print(foo.__closure__)
    print(foo.__defaults__)

def f(x):
    return x

foo = types.FunctionType(f.__code__, globals(), 'foo', f.__defaults__, f.__code__.co_varnames, f.__closure__, f.__code__.co_filename, f.__code__.co_firstlineno, f.__code__.co

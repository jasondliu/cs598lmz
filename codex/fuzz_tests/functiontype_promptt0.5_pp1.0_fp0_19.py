import types
# Test types.FunctionType

def f():
    pass

print(type(f))
print(isinstance(f, types.FunctionType))

print(dir(f))
print(f.__class__)
print(f.__code__)
print(f.__code__.co_code)
print(f.__code__.co_consts)
print(f.__code__.co_varnames)
print(f.__defaults__)
print(f.__dict__)
print(f.__doc__)
print(f.__globals__)
print(f.__closure__)
print(f.__name__)
print(f.__module__)
print(f.__qualname__)
print(f.__annotations__)

def f2(x: int):
    pass

print(f2.__annotations__)
print(f2.__annotations__['x'])
print(type(f2.__annotations__['x']))

def f3(x: int, y: str = 'hello')

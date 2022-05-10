from types import FunctionType
a = (x for x in [1])
print(type(a))

def fn(x):
    return x * x
print(isinstance(fn, FunctionType))
print(type(fn) == FunctionType)
print(callable(fn))

print(type(lambda x: x*x) == FunctionType)

print(isinstance(fn, collections.Callable))
print(type(fn) == collections.Callable)
print(callable(fn))

print(isinstance(fn, collections.Iterable))
print(type(fn) == collections.Iterable)
print(callable(fn))

print(isinstance(fn, collections.Iterator))
print(type(fn) == collections.Iterator)
print(callable(fn))

print(isinstance(fn, collections.Generator))
print(type(fn) == collections.Generator)
print(callable(fn))

print(isinstance(fn, collections.Sized))
print(type(fn) == collections.Sized)
print(callable(fn))

print(isinstance(fn, collections.Container))
print

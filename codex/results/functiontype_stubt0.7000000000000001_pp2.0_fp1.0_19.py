from types import FunctionType
a = (x for x in [1])

print(isinstance(a, FunctionType))

print(isinstance(a, Iterator))

print(isinstance(a, Generator))

print(isinstance(a, Iterable))

print(isinstance(a, list))

print(isinstance(a, dict))

class Foo:
    pass

obj = Foo()

print(isinstance(obj, Foo))

print(isinstance(obj, list))

print(isinstance(obj, FunctionType))

print(isinstance(obj, Iterable))

print(isinstance(obj, dict))

print(isinstance(obj, Iterator))

def is_iterable(param):
    return isinstance(param, Iterable)

print(is_iterable(obj))

print(is_iterable(a))

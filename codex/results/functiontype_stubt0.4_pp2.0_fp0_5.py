from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance(abs, FunctionType))
print(type(abs))
print(dir(abs))
print(abs.__name__)
print(abs.__doc__)
print(abs.__code__)
print(dir(abs.__code__))
print(abs.__code__.co_varnames)
print(abs.__code__.co_argcount)
print(abs.__code__.co_filename)
print(abs.__code__.co_code)
print(abs.__code__.co_consts)
print(abs.__code__.co_names)
print(abs.__code__.co_nlocals)

def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

print(hex(abs(-255)))

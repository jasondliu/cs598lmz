from types import FunctionType
a = (x for x in [1])
print(type(a))

def f():
    yield 1

print(type(f))
print(type(f()) == type(a))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(a, GeneratorType))

print(f.__code__.co_flags & 0x20)
print(f.__code__.co_flags & 0x80)

def f():
    pass

print(f.__code__.co_flags & 0x20)
print(f.__code__.co_flags & 0x80)

def f():
    yield 1

print(f.__code__.co_flags & 0x20)
print(f.__code__.co_flags & 0x80)

def f():
    yield from [1]

print(f.__code__.co_flags & 0x20)
print(f.__code__.co_flags & 0x80)

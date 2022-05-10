from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def f():
    yield 1

print(type(f))
print(isinstance(f, GeneratorType))
print(isinstance(f, FunctionType))

print(isinstance(f(), GeneratorType))
print(isinstance(f(), FunctionType))

print(isinstance(f, type(f())))
print(isinstance(f(), type(f)))

print(isinstance(f, type(lambda: None)))
print(isinstance(f(), type(lambda: None)))

print(isinstance(f, type(map)))
print(isinstance(f(), type(map)))

print(isinstance(f, type(filter)))
print(isinstance(f(), type(filter)))

print(isinstance(f, type(zip)))
print(isinstance(f(), type(zip)))

print(isinstance(f, type(range)))
print(isinstance(f(), type(range)))

print(isinstance(f,

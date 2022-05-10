from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def f():
    yield 1

print(type(f))
# print(type(f()))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(f, GeneratorType))
print(isinstance(f(), FunctionType))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(f, GeneratorType))
print(isinstance(f(), FunctionType))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(f, GeneratorType))
print(isinstance(f(), FunctionType))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(f, GeneratorType))
print(isinstance(f(), FunctionType))

print(isinstance(f, FunctionType))
print(isinstance(f(), GeneratorType))

print(isinstance(f, Generator

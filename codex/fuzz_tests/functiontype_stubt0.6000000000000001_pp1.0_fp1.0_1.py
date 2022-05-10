from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('-' * 20)

b = [x for x in [1]]
print(b)
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print('-' * 20)

def c():
    yield 1

print(c)
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))

print('-' * 20)

d = c()
print(d)
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))

print('-' * 20)

def e():
    yield 1
    return 2

print(e)
print(type(e))
print(isinstance(e, GeneratorType))
print(isinstance(e, FunctionType))

print('-' * 20)

f

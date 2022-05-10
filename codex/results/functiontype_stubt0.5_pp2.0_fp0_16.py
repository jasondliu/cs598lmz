from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def b():
    yield 1

print(type(b))
print(type(b()))
print(isinstance(b, FunctionType))
print(isinstance(b(), GeneratorType))

print(type(1))
print(type(None))
print(type(type(1)))

print(type(1) == int)

print(type(type) == type)

print(type(type) == type(1))

print(type(type(1)) == type(type))

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type(type(1)) == type)

print(type

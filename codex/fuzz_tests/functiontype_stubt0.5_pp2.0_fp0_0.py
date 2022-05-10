from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def my_gen():
    yield 1
    yield 2
    yield 3

a = my_gen()
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def my_gen():
    print("Generator is created")
    yield 1
    yield 2
    yield 3

a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def my_gen():
    print("Generator is created")
    yield 1
    yield 2
    yield 3

a = my_gen()
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(next(a))
print(next(a))
print(next(a))
print(next

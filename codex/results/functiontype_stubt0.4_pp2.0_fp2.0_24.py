from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == list)

print('\n')

def a():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3

b = a()
print(type(b))
print(type(b) == GeneratorType)
print(type(b) == FunctionType)
print(type(b) == list)

print('\n')

class A:
    def __iter__(self):
        print('a')
        yield 1
        print('b')
        yield 2
        print('c')
        yield 3

c = A()
print(type(c))
print(type(c) == GeneratorType)
print(type(c) == FunctionType)
print(type(c) == list)

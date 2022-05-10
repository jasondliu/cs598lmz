from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('\n')

def gen():
    yield 1

print(type(gen))
print(isinstance(gen, GeneratorType))
print(isinstance(gen, FunctionType))

print('\n')

g = gen()
print(type(g))
print(isinstance(g, GeneratorType))
print(isinstance(g, FunctionType))

print('\n')

def gen2():
    yield 1
    return

g2 = gen2()
print(type(g2))
print(isinstance(g2, GeneratorType))
print(isinstance(g2, FunctionType))

print('\n')

def gen3():
    yield 1
    yield 2
    return

g3 = gen3()
print(type(g3))
print(isinstance(g3, GeneratorType))
print(isinstance(g3, FunctionType))

print('\n')

def gen4():


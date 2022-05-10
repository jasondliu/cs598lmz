from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

from types import FunctionType
from types import GeneratorType

def gen():
    yield 1

print(isinstance(gen(), GeneratorType))
print(isinstance(gen, FunctionType))



from types import FunctionType
from types import GeneratorType

def gen():
    yield 1

def gen2():
    yield from gen()

print(isinstance(gen(), GeneratorType))
print(isinstance(gen2(), GeneratorType))
print(isinstance(gen, FunctionType))
print(isinstance(gen2, FunctionType))

a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

from types import FunctionType
from types import GeneratorType

def gen():
    yield 1

print(isinstance(gen(), GeneratorType))
print(isinstance(gen, FunctionType))



from types import FunctionType
from types import GeneratorType

def gen():
    yield 1

def gen

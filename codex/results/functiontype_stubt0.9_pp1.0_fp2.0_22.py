from types import FunctionType
a = (x for x in [1])
assert type(a) == GeneratorType
print(a)
# tworzenie list z generatora
l = [x for x in a]
print(l)

print('\n--------------')


def generator_first():
    yield 1
    yield 2


# tworzenie generatora z funkcji
g = generator_first()
assert type(g) == FunctionType
print(g)
# tworzenie list z generatora
l = [x for x in g]
print(l)

print('\n--------------')

from random import shuffle


def funkcja_iterator(args_list):
    shuffle(args_list)
    for arg in args_list:
        yield arg

g = funkcja_iterator([1,2,3,4])
print(g)
print(type(None))

print('\n--------------')
# lepiej uzywac wersji 2.7 i miec także generatorow
import sys
version = sys.version_info
if version[0] == 2:
   

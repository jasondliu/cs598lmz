from types import FunctionType
list(FunctionType(lambda: 1)(),)

print(lambda: 1)
print(FunctionType(lambda: 1, {}, '', ()))

from types import FunctionType
from pprint import pprint

glob = {}

def f(x):
    return x*x

def add_to_glob(x):
    glob['x'] = x

def f2(x):
    return glob['x'] * x

f3 = FunctionType(f.__code__, {'x': 10}, 'f3', f.__defaults__)
pprint(f3.__code__)
pprint(f3.__code__.co_freevars)
pprint(f3.__closure__)
pprint(f3(2))
print()

f4 = FunctionType(f2.__code__, {}, 'f4', f2.__defaults__, (f2.__closure__[0],))
pprint(f4.__code__)
pprint(f4.__code__.co_freevars)
pprint(f

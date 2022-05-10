from types import FunctionType
list(FunctionType(f.__code__, globals(), "f", f.__defaults__, f.__closure__))

import sys
print(sys.getrefcount(f))

f = [1, 2, 3]
print(sys.getrefcount(f))

def f():
    pass

f = [1, 2, 3]

print(sys.getrefcount(f))

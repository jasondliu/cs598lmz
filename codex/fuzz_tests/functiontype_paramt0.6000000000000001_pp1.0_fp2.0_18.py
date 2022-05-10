from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_freevars)

#

from types import FunctionType
def f():
    x = 1
    def g():
        y = 2
        def h():
            z = 3
            return (x, y, z)
        return h()
    return g()

f.__closure__[0].cell_contents

#

from types import FunctionType
def f():
    x = 1
    def g():
        y = 2
        def h():
            z = 3
            return (x, y, z)
        return h()
    return g()

#

f.__closure__[0].cell_contents

#

f.__closure__[1].cell_contents

#

def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result

#

for i in range(130):
    print(

from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_freevars)

# see the `ClosureType` class:
from types import ClosureType
list(ClosureType(lambda: 0, {}).__closure__[0].cell_contents)

# see the `FunctionType` class:
from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_freevars)

def f():
    x = 1
    y = 2
    def g():
        print(x)
        print(y)
    return g

g = f()
g()

# see the `CellType` class:
from types import CellType
print(CellType.__repr__(g.__closure__[0]))
print(CellType.__repr__(g.__closure__[1]))

# see the `CellType` class:
from types import ClosureType
ClosureType(lambda: 0, {}).__closure__[0].cell_contents

# see the `CellType` class:
from types import ClosureType


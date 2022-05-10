from types import FunctionType
list(FunctionType(0, 0, 0, 0, 0).__slots__)

# slot2
from types import FunctionType
FunctionType.__slots__ = ['foo']
FunctionType(0, 0, 0, 0, 0).foo = 1

# slot3
from types import FunctionType
def f(a, b = 1): return a
FunctionType.__slots__ = ['foo', 'bar']
f.foo = 1
f.bar = 1

# slot4
from types import FunctionType
def f(a, b = 1): return a
FunctionType.__slots__ = ['foo', 'bar']
FunctionType(0, 0, 0, 0, 0).foo = 1

# slot5
from types import FunctionType
def f(a, b = 1): return a
FunctionType.__slots__ = ['foo', 'bar']
f.__slots__ = ['baz']
f.baz = 1

# slot6
from types import FunctionType
def f(a, b = 1): return a
FunctionType.__slots__ = ['foo', 'bar']

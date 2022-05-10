from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtins__', '__file__', '__cached__', '__annotations__', '__builtin__', '__main__', '__import__', '__debug__']

# Python 3
from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtins__', '__file__', '__cached__', '__annotations__', '__builtin__', '__main__', '__import__', '__debug__']

# Python 2
from types import FunctionType
list(FunctionType(lambda: None, {}).func_globals.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtins__', '

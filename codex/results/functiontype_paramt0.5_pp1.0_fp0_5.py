from types import FunctionType
list(FunctionType(int.__add__, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'types', '__builtin__', '__all__', '__docformat__', 'sys', 'inspect']

# for the function itself

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'types', '__builtin__', '__all__', '__docformat__', 'sys', 'inspect', 'FunctionType', '__defaults__', '__closure__', '__code__', '__globals__', '__dict__', '__weakref__', '__module__']

# for the function itself

# ['__name__', '__doc__', '__package__', '__loader__', '__spec

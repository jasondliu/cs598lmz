from types import FunctionType
list(FunctionType(m.__code__, globals()).__globals__.keys())

# ['__name__',
#  '__doc__',
#  '__package__',
#  '__loader__',
#  '__spec__',
#  '__annotations__',
#  '__file__',
#  '__cached__',
#  '__builtins__']

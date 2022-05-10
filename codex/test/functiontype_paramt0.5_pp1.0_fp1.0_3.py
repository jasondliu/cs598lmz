from types import FunctionType
list(FunctionType(f.__code__, globals(), "f") for f in [lambda: 1, lambda: 2, lambda: 3])

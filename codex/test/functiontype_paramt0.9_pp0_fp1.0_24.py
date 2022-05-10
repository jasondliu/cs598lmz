from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f') for f in (lambda: None, lambda: None))

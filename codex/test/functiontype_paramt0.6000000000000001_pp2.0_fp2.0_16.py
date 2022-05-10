from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__)
     for f in [lambda: None, lambda: None])[0]

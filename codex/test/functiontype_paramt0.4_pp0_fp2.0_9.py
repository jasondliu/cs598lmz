from types import FunctionType
list(FunctionType(f.__code__, globals(), name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__)()
     for f in [lambda: 1, lambda: 2, lambda: 3])
# [1, 2, 3]

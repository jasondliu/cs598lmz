from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda: None,))

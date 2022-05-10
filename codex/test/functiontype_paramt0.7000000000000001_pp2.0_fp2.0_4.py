from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
              argdefs=f.__defaults__,
              closure=f.__closure__) for _, f in globals().items()
    if isinstance(f, FunctionType))

# получаем все функции с класса
from types import FunctionType
from inspect import signature
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
              argdefs=f.__defaults__,
              closure=f.__closure__) 
    for _, f in globals().items()
    if isinstance(f, FunctionType) and 'self' in signature(f).parameters)

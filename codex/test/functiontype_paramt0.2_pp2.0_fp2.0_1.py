from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)),
               lambda x=5: (yield from range(x))))
# [<function <lambda> at 0x7f6f9c7b4c80>,
#  <function <lambda> at 0x7f6f9c7b4d08>]

# The following is a more general solution that works for any function.
# It requires the `inspect` module, which is not available on all platforms.
from inspect import getclosurevars
def copy_func(f, name=None):
    """Return a shallow copy of a function.
    """
    name = name or f.__name__
    closure = getclosurevars(f).nonlocals
    return FunctionType(f.__code__, f.__globals__, name,
                        f.__defaults__, closure)


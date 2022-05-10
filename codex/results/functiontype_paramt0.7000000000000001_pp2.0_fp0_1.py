from types import FunctionType
list(FunctionType("f", globals(), None, None, None))
# [<function __init__>, <function __new__>, <function __call__>]
type("f")
# <type 'str'>
type("f").__name__
# 'str'

import sys
sys.modules["__main__"].__dict__.keys()
# ['__builtins__', '__doc__', '__name__', ...]

from fractions import gcd
gcd.__globals__["__builtins__"].__dict__.keys()
# ['BaseException', 'ArithmeticError', 'AssertionError', ...]


def f():
    def g():
        def h():
            pass
        h()
    g()

f.__closure__
# (None, None, <cell at 0x00C3CD68: function object at 0x00C3C9B0>)

f.__closure__[2].cell_contents
# <function h at 0x00C2C9B0>


def createGenerator(N):
    for n in range(

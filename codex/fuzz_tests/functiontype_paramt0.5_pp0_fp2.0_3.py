from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name='f', argdefs=(), closure=f.__closure__))

[<function f at 0x7f7c9a9087b8>]

In [8]: g = lambda x: x

In [9]: list(FunctionType(g.__code__, g.__globals__, name='g', argdefs=(), closure=g.__closure__))
Out[9]: [<function <lambda> at 0x7f7c9a9087a8>]

In [10]: h = lambda x, y: x + y

In [11]: list(FunctionType(h.__code__, h.__globals__, name='h', argdefs=(), closure=h.__closure__))
Out[11]: [<function <lambda> at 0x7f7c9a9087d0>]

In [12]: i = lambda x, y, z: x + y + z

In [13]: list(FunctionType(i.__code__, i.

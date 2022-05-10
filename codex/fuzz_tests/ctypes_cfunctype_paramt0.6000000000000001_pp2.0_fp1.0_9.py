import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def bar(a):
    return a + 1

CALLBACK = FUNTYPE(bar)

def foo(a):
    return bar(a) + 1

CALLBACK2 = FUNTYPE(foo)
</code>
The second callback fails with:
<code>TypeError: don't know how to convert function 'foo' to parameter type FUNTYPE
</code>
Is there a way to make the second callback work?


A:

It's a very good question.
The problem is that ctypes does not support decorators (so far). So you have to define the decorated function in a way that you can pass it to the decorator. A common way to do this is using <code>functools.partial</code>:
<code>import ctypes
from functools import partial

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CALLBACK = FUNTYPE(partial(bar))
</code>


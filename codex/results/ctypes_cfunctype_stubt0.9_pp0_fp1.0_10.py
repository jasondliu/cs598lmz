import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    yield from [0,1]
</code>
and then <code>fun()</code>, you get <code>TypeError: generator returned non-None</code> as expected.
However, if you try to send anything to a generator return by <code>fun()</code> you get a crash or a stale pointer; it appears that some internal data has magically gone out of sync. It's tempting to think that <code>yield</code> and the like need to be kept apart from C code, given their delicate nature, but unrelated C code errors don't appear to exhibit this behavior:
<code>@FUNTYPE
def fun1():
    x = None
    x.foo
fun1()
</code>
yields an <code>AttributeError</code> as expected. And "C <code>yield</code>" does work:
<code>@FUNTYPE
def fun2():
    yield
    yield
    yield
next(fun2())
next(fun2())
</code>
So is this a bug, or am I doing something wrong?


import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)

class Test(ctypes.Structure):
    _fields_ = [("func", FUNTYPE)]

test = Test()
test.func = FUNTYPE(lambda x: x + 1)
</code>
Which works as expected. But I would like to be able to do something like this:
<code>def foo(x):
    return x + 1

test = Test()
test.func = FUNTYPE(foo)
</code>
But this fails with the error:
<code>TypeError: an integer is required
</code>
I've also tried:
<code>test.func = FUNTYPE(foo())
</code>
and
<code>test.func = FUNTYPE(&amp;foo)
</code>
But both fail with:
<code>TypeError: wrong type
</code>
Is it possible to do what I want, and if so, how?
I'm using Python 2.7.1 on 64-bit Ubuntu 11.04.


A:

Use <code>ctypes.CFUN

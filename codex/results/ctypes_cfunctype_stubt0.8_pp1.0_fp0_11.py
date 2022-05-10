import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert fun().value == 1
assert fun().value == 1
assert fun().value == 1
</code>
Even though the return value is of a simple type, the first two calls fail because the memory is released.
The only way I got to make it work is to return a string:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "1"

assert fun().value == "1"
assert fun().value == "1"
assert fun().value == "1"
</code>
I don't understand why the string works and the integer does not. I tried to experiment with the <code>__del__</code> method of the integer but it doesn't seem right.


A:

The memory is not being released.
The problem is that you're creating a new instance of <code>int</code> on each call, and then discarding it.
<code>&gt;&gt;&gt; def fun():
...     return 1
...
&gt;&gt;&

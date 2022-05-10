import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'a'
</code>
When I run this code in the interpreter, it runs fine.
<code>&gt;&gt;&gt; fun()
'a'
</code>
However, when I run this code from a script, it crashes.
<code>$ python fun.py
Segmentation fault
</code>
I'm running Python 2.7.10 on Ubuntu 14.04.
Can someone help me understand what's going on here?


A:

The problem is that the interpreter is built with <code>-fwrapv</code> which makes Python's <code>int</code> behave like a two's complement wrapped-around type.
Since you are returning a Python object, the return value is an <code>int</code> that refers to the object.  That is, the return value is the address of the object.  The <code>int</code> is a large positive number that wraps around to a negative number.  The <code>CFUNCTYPE</code> assumes that the <code>int</code> is a signed number, so it is cast to a signed number and the result

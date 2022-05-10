import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ...
@fun()
def foo(x):
    print(x)
foo(1)
</code>
It works as intended (that is, it prints <code>1</code>).
However, I was wondering whether it would be possible to do this without explicitly calling <code>fun</code> in <code>foo</code>'s definition. That is, I thought it would be possible to write a decorator, say <code>dec</code>, that would make the following code work as if it were the code above:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ...
@dec
def foo(x):
    print(x)
foo(1)
</code>
Is this possible at all?
This was tested on Python 3.6.7.


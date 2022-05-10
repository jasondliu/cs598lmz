import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = 25
    y = 2
    z = x + y
    a = x % y
    b = y // x
    c = x * y
    d = x - y
    e = x / y
    return [z, a, b, c, d, e]

fun()
</code>
Notice I am calling the function <code>fun</code> at the bottom of the code, but nothing is printed.
Any reason why the function is not actually doing anything?


A:

You are returning a list, so you need to iterate over it to print all the values:
<code>for x in fun():
    print(x)
</code>
or
<code>print(*fun(), sep='\n')
</code>


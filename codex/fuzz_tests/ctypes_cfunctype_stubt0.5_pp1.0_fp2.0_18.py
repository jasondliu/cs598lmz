import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

def g():
    return f()

it = g()
for i in it:
    print(i)
</code>
The output is:
<code>1
1
1
1
1
1
1
1
1
1
</code>


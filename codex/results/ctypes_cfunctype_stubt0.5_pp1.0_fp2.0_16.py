import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def f():
    return fun()

def g():
    return f()

def main():
    print g()

main()
</code>
When I run this, it crashes.  I have a core dump.  I'm not sure how to interpret it, but it seems to be crashing in the <code>PyObject_Call</code> function.
<code>#0  0x00007ffff7b9f9e8 in PyObject_Call () from /usr/lib/libpython2.7.so.1.0
#1  0x00007ffff7b8aeea in PyEval_EvalFrameEx () from /usr/lib/libpython2.7.so.1.0
#2  0x00007ffff7b8d1f3 in PyEval_EvalCodeEx () from /usr/lib/libpython2.7.so.1.0
#3  0x00007ffff7b8d2b5 in PyEval_EvalCode () from /usr/lib/libpython2.7.so.1.0


import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())

class A:
    def __init__(self):
        self.a = fun

a = A()
print(a.a())
</code>
Why does this give me a <code>Fault: segmentation violation</code> error?
I am running on a Raspberry pi, in a venv.


A:

The problem is that the function you are returning is a C function, and you are trying to return it to the Python interpreter.
Python does not know what to do with it, and thinks you are trying to return a pointer.


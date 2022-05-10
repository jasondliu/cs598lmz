import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
print(fun())
</code>
I get the following error when running the code:
<code>Fatal Python error: Segmentation fault</code>
I am running python 3.7.2 in Ubuntu 18.04.


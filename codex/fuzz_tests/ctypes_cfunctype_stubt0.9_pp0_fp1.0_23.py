import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun python called")

lib = ctypes.CDLL("build/libtest.so")
lib.setcallback(FUNTYPE(fun))
lib.call_python_callback(1)
</code>
For a better explanation of why I would consider doing this read this post.


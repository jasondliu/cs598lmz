import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return bytes(object)
</code>
As you can see, I tried casting object to bytes, but obviously it doesn't work. What can I do?


A:

You cannot return a python object from an extension function.  I'm not sure why you want to do this, but it's not a sensible thing to try.


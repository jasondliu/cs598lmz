import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise OSError("a")
</code>
then you can use <code>ctypes.set_conversion_mode("ascii")</code> to get the function to raise an exception.


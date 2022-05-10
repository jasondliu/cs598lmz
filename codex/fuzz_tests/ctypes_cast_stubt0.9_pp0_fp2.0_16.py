import ctypes
ctypes.cast(ctypes.c_void_p.from_param(23), ctypes.py_object)
# &lt;__main__.LP_py_object object at 0x7f87145c7930&gt;
ctypes.cast(23, ctypes.py_object)
# &lt;__main__.LP_py_object object at 0x7f87145c7930&gt;
ctypes.cast(23, ctypes.py_object).value
# 23
</code>
However, using <code>py_object</code> doesn't seem to allow taking the address of the wrapped object. So this seems to be a dead end for you.
How to make <code>ctypes.cast(b' \x08\x00\x00\x00\x10\x00\x00\x00', ctypes.py_object).value</code> print out 2 ?


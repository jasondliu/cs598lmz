import ctypes
ctypes.cast(0, ctypes.py_object).value
</code>
Because of the "unconstrained" nature of Python's object model, it's hard to get this wrong.  It's also, as you can see, hard to use correctly.


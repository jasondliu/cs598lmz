import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
It does not raise.
However, if I try to cast it to another type:
<code>ctypes.cast(0, ctypes.c_char_p)
</code>
It raises <code>TypeError: int() argument must be a string or a number, not 'NoneType'</code> which should be quite expected.
I cannot figure out, however, why the first case did not raise.
Is there any particular reason why casting a bad ctypes pointer to <code>py_object</code> doesn't raise?


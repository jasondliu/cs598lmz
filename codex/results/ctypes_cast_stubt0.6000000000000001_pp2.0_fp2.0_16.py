import ctypes
ctypes.cast(0x12345678, ctypes.c_void_p).value

# the next line fails:
ctypes.cast(0x12345678, ctypes.c_void_p).value = 0x87654321
</code>
The error message is:
<code>Traceback (most recent call last):
  File "&lt;pyshell#4&gt;", line 1, in &lt;module&gt;
    ctypes.cast(0x12345678, ctypes.c_void_p).value = 0x87654321
AttributeError: attribute 'value' of '_ctypes.PyCPointerType' objects is not writable
</code>
So basically, is there any way to cast a Python integer to a ctypes pointer type such that it is writable?


A:

<code>ctypes</code> is intended to be used with pointers obtained from the C side.  It doesn't really make sense to try to use it with a Python integer.  If you want to use a Python integer to store a pointer value, you can use <code>ctypes

import ctypes
ctypes.cast(0, ctypes.py_object)
# Segmentation fault
</code>
I've also tried:
<code>import ctypes
ctypes.cast(0, ctypes.c_void_p).value
# 0
</code>
But I don't know how to convert that back to a <code>PyObject*</code>.
What is the correct way to do this?


A:

You can't, because it's an invalid pointer.  If you try to use it, you'll get a segmentation fault.  The only way to get a pointer to an integer is to allocate memory for it.


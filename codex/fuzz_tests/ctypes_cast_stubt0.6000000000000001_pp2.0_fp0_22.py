import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
The <code>ctypes</code> module does not support GC and, therefore, does not support object-to-object casts.


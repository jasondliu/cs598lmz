import ctypes
ctypes.cast(id(xxx), ctypes.py_object).value.x = 5
</code>
This is equivalent to:
<code>xxx.x = 5
</code>


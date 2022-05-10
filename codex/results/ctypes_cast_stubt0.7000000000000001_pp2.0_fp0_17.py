import ctypes
ctypes.cast(pointer, ctypes.py_object).value = new_value
</code>
Here's a non-<code>ctypes</code> version using the <code>ctypes</code> structure and <code>struct</code> module to do the same thing:
<code>import ctypes
import struct
# ...
pointer = ctypes.cast(pointer, ctypes.c_void_p).value
new_value = '&lt;new string value&gt;'
struct.pack_into(ctypes.sizeof(ctypes.py_object), pointer, 0, new_value)
</code>
You can't just cast the pointer to a <code>ctypes.py_object</code> and update it in-place because <code>ctypes.py_object</code> is a pointer to a PyObject*, not a PyObject*. If you tried to use it as a pointer to a PyObject, it would point to the wrong place in memory.


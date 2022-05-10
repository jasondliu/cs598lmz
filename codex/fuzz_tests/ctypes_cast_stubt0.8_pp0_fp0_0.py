import ctypes
ctypes.cast(ptr, ctypes.py_object).value = frame #replace pointer to frame with the frame
</code>
this is not a reference to the frame inside the callee, but the real frame with all its values.
(I would use this, for example for threading)


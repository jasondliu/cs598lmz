import ctypes
ctypes.cast(py_object, ctypes.py_object)

# TypeError: must be a ctypes object pointer, not object
</code>
I would like to be able to do this without using the <code>ctypes.pythonapi</code> module.
<code># This works, but uses the ctypes.pythonapi module
import ctypes

ctypes.pythonapi.PyCapsule_New.restype = ctypes.py_object
ctypes.pythonapi.PyCapsule_New.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]

capsule = ctypes.pythonapi.PyCapsule_New(ctypes.py_object(1), None, None)
capsule

# &lt;capsule object "None" at 0x7f8b2c78ba40&gt;
</code>


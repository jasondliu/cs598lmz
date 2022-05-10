import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("x", ctypes.c_int)]
</code>
In CPython, this raises the <code>ValueError</code> <code>Structure has two fields with the same name: 'x'</code>.  In PyPy, it raises the <code>ValueError</code> <code>Structure has two fields with the same name: ('x', &lt;class 'ctypes.c_int'&gt;)</code>.
There are some other edge cases where certain ctypes definitions could be valid in CPython and not PyPy.  For example, this is valid in CPython:
<code>class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("x", ctypes.c_int)]
    y = ctypes.c_int
</code>
But it is not valid in PyPy.  PyPy only allows a field in <code>_fields_</code> to be defined once.  If you want to access the same field multiple times, you

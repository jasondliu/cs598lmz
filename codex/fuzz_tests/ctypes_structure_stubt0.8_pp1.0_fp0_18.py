import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_OptimizeFlag")

print(S.x)
</code>
This prints out the value of <code>Py_OptimizeFlag</code>. 
It's worth noting that this way of getting the value is not guaranteed to work across Python versions. The use of <code>pythonapi</code> is de facto not official. But it works as long as you don't care about new versions of Python.


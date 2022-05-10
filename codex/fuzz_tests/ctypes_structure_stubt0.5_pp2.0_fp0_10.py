import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_RefTotal')
    y = ctypes.c_int.in_dll(ctypes.pythonapi, '_Py_RefTotal')

print S().x
print S().y
</code>


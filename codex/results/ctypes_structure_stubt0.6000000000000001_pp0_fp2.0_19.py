import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double.in_dll(ctypes.pythonapi, '_Py_NotImplementedStruct')

print(S.x)
</code>
Output:
<code>c_double(7.2911220189721939e-304)
</code>
(The value is different for me, it may depend on Python's version and what compiler was used)


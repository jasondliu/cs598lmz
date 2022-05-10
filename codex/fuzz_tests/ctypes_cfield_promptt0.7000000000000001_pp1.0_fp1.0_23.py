import ctypes
# Test ctypes.CField
class CTestStruct(ctypes.Structure):
    _fields_ = [
        ('_a', ctypes.c_int),
        ('_b', ctypes.c_int),
        ('_c', ctypes.c_int),
    ]
    a = ctypes.CField('_a')
    b = ctypes.CField('_b')
    c = ctypes.CField('_c')

obj = CTestStruct(5, 4, 3)
print(obj.a)
# 5
print(obj.b)
# 4
print(obj.c)
# 3
</code>


import ctypes

class S(ctypes.Structure):
    x = ("abc", ctypes.c_int)  # non-homogeneous item

S._fields_ = S._get_field_types_()
</code>


import ctypes
# Test ctypes.CField
c_float._fields_ = [("x", ctypes.c_float),
                    ("y", ctypes.c_float),
                    ("z", ctypes.c_float)]

print(c_float.x)
print(c_float.y)
print(c_float.z)

print(c_float.__dict__)
print(dir(c_float))

print(c_float.__sizeof__())

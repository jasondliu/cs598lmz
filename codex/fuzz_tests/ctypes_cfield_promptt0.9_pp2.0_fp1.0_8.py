import ctypes
# Test ctypes.CField


class X(ctypes.Structure):
    _fields_ = [("first_field", ctypes.c_int),
                ("_internal", ctypes.c_int),
                ("last_field", ctypes.c_int)]


x = X(1, 2, 3)
print("Regular fields:", x.first_field, x.last_field)
print("An internal field:", x._internal)

x.first_field = 4
x._internal = 5
x.last_field = 6

print("Modified fields:", x.first_field, x.last_field)
print("Modified internal:", x._internal)
print("Initial fields:", x.first_field, x.last_field)
print("Initial internal:", x._internal)
x.first_field = -4
x._internal = -5
x.last_field = -6

print("Modified fields:", x.first_field, x.last_field)
print("Modified internal:", x._internal)
print("Initial fields:", x.first_field

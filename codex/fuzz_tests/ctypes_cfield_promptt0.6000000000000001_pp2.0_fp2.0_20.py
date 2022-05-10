import ctypes
# Test ctypes.CField.
#
# This example is from the book "Python in a Nutshell, Second Edition".
# It is written by Alex Martelli, and owned by O'Reilly Media, Inc.
class FIELD(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char * 16),
        ("type", ctypes.c_char * 16),
        ("size", ctypes.c_int),
        ("offset", ctypes.c_int),
    ]

f1 = FIELD(b"name1", b"type1", 1, 1)
f2 = FIELD(b"name2", b"type2", 2, 2)
f3 = FIELD(b"name3", b"type3", 3, 3)

f = FIELD(b"name", b"type", 3, 3)
print(f)

f.name = b"name4"
f.type = b"type4"
f.size = 4
f.offset = 4
print(f)

# The following is an error.
f.size = "

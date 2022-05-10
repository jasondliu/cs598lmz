import ctypes
# Test ctypes.CField
class FIELD(ctypes.Structure):
    _fields_ = [("f1", ctypes.c_int),
                ("f2", ctypes.c_int)]

class Container(ctypes.Structure):
    _fields_ = [("array", FIELD * 3),          # array of 3 elements
                ("pointer", ctypes.POINTER(FIELD))]

c = Container()

c.array[0].f1 = 1
c.array[0].f2 = 2
c.array[1].f1 = 3
c.array[1].f2 = 4
c.array[2].f1 = 5
c.array[2].f2 = 6

c.pointer = ctypes.pointer(c.array[2])

print("array:", list(c.array))
print("pointer:", c.pointer.contents)
print("pointer:", c.pointer[0])

# Test ctypes.Array
class ARRAY(ctypes.Structure):
    _fields_ = [("array", ctypes.c_int * 3)]    #

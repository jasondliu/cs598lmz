import ctypes
# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

p = Point(1, 2)

# Test ctypes.PyCFuncPtr
def print_point(point):
    print("({x}, {y})".format(x=point.x, y=point.y))

print_point_ptr = ctypes.CFUNCTYPE(None, ctypes.POINTER(Point))(print_point)

# Test ctypes.PyCPointer
print_point_ptr(p)

# Test ctypes.PyCSimpleType
ctypes.c_int

# Test ctypes.PyCStructType
ctypes.Structure

# Test ctypes.PyCThunkObject
ctypes.c_int.__ctypes_from_outparam__

# Test ctypes.PyCArrayType
ctypes.c_int * 10

# Test ctypes.PyCArg_ParseTupleAndKeywords
ctypes

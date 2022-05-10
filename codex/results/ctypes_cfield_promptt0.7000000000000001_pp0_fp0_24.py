import ctypes
# Test ctypes.CField
# Create a C structure
class POINT(ctypes.Structure):
	_fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

# Create a pointer to the structure
pt = POINT(10, 20)
print(pt.x, pt.y)
# Get a pointer to the C++ class
# as a ctypes.CField
ptr = ctypes.CField(POINT, 'ptr', ctypes.POINTER(POINT))
# Create a new structure and set the pointer field
p = POINT()
ptr.set(p, pt)
print(p.ptr.contents.x, p.ptr.contents.y)

import ctypes
# Test ctypes.CField.
class X(ctypes.Structure):
	_fields_ = [("y", ctypes.c_int),
							("z", ctypes.c_int)]
	
	y = ctypes.CField(lambda x: x.z)

print X.y.__doc__

# Test ctypes.CField.
class X(ctypes.Structure):
	_fields_ = [("y", ctypes.c_int),
							("z", ctypes.c_int)]
	
	y = ctypes.CField(lambda x: x.z)
	y.__doc__ = "Hello"
	
	
print X.y

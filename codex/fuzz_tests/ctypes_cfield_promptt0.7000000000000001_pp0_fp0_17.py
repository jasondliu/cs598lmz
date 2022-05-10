import ctypes
# Test ctypes.CField.
class Test(ctypes.Structure):
	_fields_ = [("value", ctypes.c_int),
	            ("data", ctypes.c_void_p, 32)]
	_anonymous_ = ["data"]
	def __init__(self, value=0):
		self.value = value
# Using _fields_, _anonymous_, __init__ and __repr__,
# we have a complete mapping of the C-structure to Python.
t = Test(10)
print t
print t.value
print t.data

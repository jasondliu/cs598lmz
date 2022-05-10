import ctypes
# Test ctypes.CFUNCTYPE
# Only the return type is significant for ctypes, the arguments
# can be anything at all.
PyObject = ctypes.py_object
f = ctypes.CFUNCTYPE(PyObject)(lambda x: x)
print "f.argtypes ->", f.argtypes
print "f.restype ->", f.restype
print f(1) == 1
print f("hello") == "hello", "\n"
# Try it with a foreign function type.
conv = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)
# Assume a function add_furniture exists that takes one float argument and
# returns one int result.
add_furniture = conv(add_furniture)
print "add_furniture.argtypes ->", add_furniture.argtypes
print "add_furniture.restype ->", add_furniture.restype
print add_furniture(3.14) == 3
print "\n"
# Test ctypes.
p1 = Point(x=1,y=2

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 5
def f():
	return 5

cfunc = FUNTYPE(f)
print(fun(), cfunc())

# convert a python object to ctypes
class StructTest(ctypes.Structure):
	_fields_ = [
		('x', ctypes.c_int),
		('y', ctypes.c_double)
	]
obj = StructTest(5, 3.14)
print(obj.x, obj.y)

s = {'x': 5, 'y': 3.14}
obj = StructTest(**s)
print(obj.x, obj.y)


# Use a ctypes array type.
# reference: https://docs.python.org/3/library/ctypes.html#arrays
ARRAY6 = ctypes.c_int*6
arr = ARRAY6(*range(6))
print(arr)

# reference: https://docs.python.org/3/library/ctypes.html#contents
class StructPointer(ctypes.Structure):
	_fields_ = [
		('

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	print(1)
	return 1
class A:
	pass
a = A()
a.name = 'fun'
a.fun = fun
print(a.fun())
print(a.name)

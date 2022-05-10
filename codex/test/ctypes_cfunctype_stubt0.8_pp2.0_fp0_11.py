import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return "fun"
def fun2():
	return "fun2"

def fun3():
	return "fun3"

def fun4():
	return "fun4"
fun3.__dict__['__name__'] = "fun3"
fun3.__dict__['__doc__'] = "fun3 doc"
fun4.__name__ = "fun4"
fun4.__doc__ = "fun4 doc"
fun5 = lambda: "fun5"
fun5.__name__ = "fun5"
fun5.__doc__ = "fun5 doc"


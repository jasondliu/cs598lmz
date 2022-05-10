import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	print "hahahahah!"
	return 1
fun()
print fun.__name__
#print fun.__class__
#print type(fun)
#from ctypes import cdll
#lib_fun = cdll.LoadLibrary('')
#error: could not open library '': No such file or directory

import test1
print test1.fun(10)

x = 10
if x < 20:
	print str(x) + " is less than 20"
#print locals()
#print globals().keys()
#print globals().values()
#print globals()['__builtins__']
#print __builtins__.keys()
#print __builtins__.values()
#print __builtins__['divmod']
#print __builtins__.divmod(10,3)
#print __builtins__.__name__
#print __builtins__.__class__
#print __builtins__.__doc__
#print __builtins__.__globals__
#print __builtins__.fun(10)
#no attribute 'fun

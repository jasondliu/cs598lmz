import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return ()

def func():
	pass

def func(a):
	pass

def func(a,b):
	pass

def func(a,b,c:int=0,*args,**kwargs):
	pass

def func(a,b,c,d:int=0,*args,**kwargs):
	pass

def func(a,b,c,d,*args,e,f,g):
	pass


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

def func(a,b,c,d,*args,e,f,g,h,*args2):
	pass

def func(a,b,c,d,*args,e,f,g,h,*args2,i:int=0,j:int=0,**kwargs):
	pass

def func(a,b,c,d,*args,e,f,g,h,*args2,i:int=0,j:int=0,**kwargs):
	pass

def func(a,b,c,d,*args,e,f,

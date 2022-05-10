import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)
func = FUNTYPE(myfunc)
p = [1,.1,.01]
##x = ctypes.c_double()
x = 0.1

def F1(xx=[]):
	global p
	x = xx[0]
	omega = xx[1]
	fi = xx[2]
	return p[0]*x - p[1]*x*omega + p[2]*math.sin(fi)

def F2(xx=[]):
	global p
	x = xx[0]
	omega = xx[1]
	fi = xx[2]
	return p[1]*x*omega - p[2]*math.sin(fi)

def F3(xx=[]):
	global p
	x = xx[0]
	omega = xx[1]
	fi = xx[2]
	return p[1]*x - p[2]*math.cos(fi)

def Jacobian(xx=[],h = 1

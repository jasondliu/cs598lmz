import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def mysin(x):
    return math.sin(x)

def mycos(x):
    return math.cos(x)

def myexp(x):
    return math.exp(x)

def mylog(x):
    return math.log(x)

func_list = [mysin, mycos, myexp, mylog]

for f in func_list:
    fp = FUNTYPE(f)
    print(fp(1))

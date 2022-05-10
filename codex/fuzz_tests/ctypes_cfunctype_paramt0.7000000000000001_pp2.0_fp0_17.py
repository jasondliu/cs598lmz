import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def myFun(x):
    a = 2.0
    b = 0.5
    return a*x + b

myFunPtr = FUNTYPE(myFun)

c = ctypes.CDLL('C:\\Users\\Max\\Documents\\GitHub\\3rdSemester\\DSP2\\c_code\\module_c.dll')

c.func_module_c.argtypes = (FUNTYPE, ctypes.c_int, ctypes.c_double)
c.func_module_c.restype = ctypes.POINTER(ctypes.c_double)

n = 5
x = 0.5
res = c.func_module_c(myFunPtr, n, x)
for i in range(n):
    print(res[i])
print()
for j in range(n):
    print(myFun(x))
    x += 1

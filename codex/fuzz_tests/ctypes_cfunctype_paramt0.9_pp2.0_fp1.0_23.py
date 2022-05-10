import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_float,ctypes.c_float)

def integrate(f,a,b,h):
    tmp = 0.0
    for i in range(1,int((b-a)/h)+1):
        tmp = tmp + f(a+h*(i-0.5),h)
    return h*tmp
func_sum = ctypes.CDLL('./libsum.so')
sum_ = func_sum.sum_
sum_.restype = ctypes.c_float
sum_.argtypes = (FUNTYPE,ctypes.c_float,ctypes.c_float,ctypes.c_float)
x = integrate(lambda x,h: np.sin(x)/2,0,PI,0.01)
print(x)
x = sum_(lambda x,h: np.sin(x)/2,0,PI,0.01)
print(x)
x = sum_(lambda x,h: np.sin(x)/2,0,PI,0.01)
print(x)
</code>

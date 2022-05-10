import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def f1(x): return x+1
def f2(x): return x*2
f = FUNTYPE(f1)
g = FUNTYPE(f2)
print(f(3), g(3))
print(f.address, g.address)
print(callback(4, f), callback(4, g))

# 3) C++ to C++
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def f1(x): return x+1
def f2(x): return x*2
f = FUNTYPE(f1)
g = FUNTYPE(f2)
print(callback(4, f), callback(4, g))

# 4) C++ to Python
print(callback(3))

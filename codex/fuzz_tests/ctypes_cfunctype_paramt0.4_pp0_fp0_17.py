import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x*x

f_c = FUNTYPE(f)
print(f_c(2.0))

def g(x):
    return f(x) + 1

g_c = FUNTYPE(g)
print(g_c(2.0))

def h(x):
    return f(x) + f(x+1)

h_c = FUNTYPE(h)
print(h_c(2.0))

def i(x):
    return f(x) + g(x)

i_c = FUNTYPE(i)
print(i_c(2.0))

def j(x):
    return f(x) + g(x+1)

j_c = FUNTYPE(j)
print(j_c(2.0))

def k(x):
    return f(x) + h(x)

k_c = FUNTYPE(k)
print(k_c(2.0))

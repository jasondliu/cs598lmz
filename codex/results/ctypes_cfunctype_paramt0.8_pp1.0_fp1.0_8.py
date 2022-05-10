import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# def myfun(x):
#     return x**2
#
# fptr = FUNTYPE(myfun)
# print(fptr(15))
# print(fptr(2.6))

def myfun(x):
    return math.sin(x)

fptr = FUNTYPE(myfun)
print(fptr(15))
print(fptr(2.6))

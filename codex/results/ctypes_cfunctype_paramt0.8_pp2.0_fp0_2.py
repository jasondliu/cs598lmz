import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
ptr = ctypes.cast(libm.printf, FUNTYPE)
print("printf address: ", ptr)
ptr()

# we can also create instance of functype class
def fun1():
    print("fun1 was called")
cfun1 = FUNTYPE(fun1)
print("cfun1 address: ", cfun1)
cfun1()

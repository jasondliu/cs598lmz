import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

#load DLL
mydll = ctypes.CDLL("mydll.dll")

#get function's address.
mydll.add.restype = ctypes.c_int
mydll.sum.restype = ctypes.c_int

#declare prototype of sum
sum_ = FUNTYPE(("sum",mydll),((1, "a"),(1,"b")))

#call the function in the dll
print("1 + 2 = %d\n3 + 4 = %d" % (mydll.add(1,2),mydll.sum(3,4)))

#call the function prototype declared above.
print("5 + 6 = %d" % sum_(5,6))

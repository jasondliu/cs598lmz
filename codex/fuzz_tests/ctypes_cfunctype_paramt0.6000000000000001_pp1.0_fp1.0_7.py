import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# get the handle to the dll
mydll = ctypes.windll.LoadLibrary("mydll.dll")

# get the address of the dll function
mydll.mydll_f.argtypes = (ctypes.c_int, ctypes.c_int)
mydll.mydll_f.restype = ctypes.c_int
f = mydll.mydll_f

# create a function f_py in Python which looked exactly like the function f in the dll
f_py = FUNTYPE(f)

# call the function f_py
print(f_py(2,3))
</code>


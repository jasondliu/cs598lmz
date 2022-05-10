import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# import the compiled module
import myModule

# create a python function that calls the C function
python_function = FUNTYPE(myModule.myModule.fct)

# call the function
print python_function()

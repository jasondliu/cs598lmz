import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_double)

# Fetch the path of the script:
scr_path = os.path.dirname(__file__)
if not scr_path:
    scr_path = '.' + os.sep
    
# Load the C++ script:
fun_wrapper = ctypes.CDLL(scr_path + 'fun_wrapper.so')

# Take an address of the 'fun' function in the script:
fun_wrapper.function.argtypes = [FUNTYPE]

# The function that we pass to the C++ script:
def fun(x):
    return (x + 2)**2


# Make the function "callable" by the C++ script:
fb1 = FUNTYPE(fun)

# Call the C++ script:
print(fun_wrapper.fuction(fb1, 1))
```

By the way, `fun_wrapper.so` (a C++ script library) will be compiled automatically by ccglue.

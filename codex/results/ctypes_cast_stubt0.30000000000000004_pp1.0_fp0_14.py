import ctypes
ctypes.cast(0, ctypes.py_object).value

# Initialize the "ctypes" and the "c_float" data type
import ctypes
import ctypes.util
c_float_p = ctypes.POINTER(ctypes.c_float)

# Load the shared object file
c_lib = ctypes.CDLL(ctypes.util.find_library('c'))

# Set the argtypes
c_lib.sin.argtypes = [ctypes.c_float]

# Set the restype
c_lib.sin.restype = ctypes.c_float

# Call the C sin function
print(c_lib.sin(1.0))

# Initialize ctypes
import ctypes

# Load a shared object file
c_lib = ctypes.CDLL('./c_code.so')

# Set argtypes
c_lib.my_function.argtypes = (ctypes.c_int, ctypes.c_int)

# Set restype
c_lib.my_function.restype = ctypes.c_int


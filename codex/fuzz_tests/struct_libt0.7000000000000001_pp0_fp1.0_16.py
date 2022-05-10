import _struct
print("\n=======================\n")
print(">> import _struct")
print("\n=======================\n")

# Imports the ctypes library.
import ctypes
print("\n=======================\n")
print(">> import ctypes")
print("\n=======================\n")

# Loads the OpenCL C shared library.
_opencl = ctypes.cdll.LoadLibrary("libOpenCL.so")
print("\n=======================\n")
print(">> _opencl = ctypes.cdll.LoadLibrary(\"libOpenCL.so\")")
print("\n=======================\n")

# Defines the ctypes variable types to match the OpenCL C variable types.
cl_char = ctypes.c_char
cl_uchar = ctypes.c_ubyte
cl_short = ctypes.c_short
cl_ushort = ctypes.c_ushort
cl_int = ctypes.c_int
cl_uint = ctypes.c_uint
cl_long = ctypes.c_long

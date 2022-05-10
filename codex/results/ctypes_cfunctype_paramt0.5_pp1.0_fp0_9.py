import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.c_int )

# wrapped function
def my_func( a, b ):
    return a + b

# wrap my_func
my_func_wrapper = FUNTYPE( my_func )

# call my_func
print( my_func_wrapper( 1, 2 ) )

# call my_func from C
libc = ctypes.CDLL( None )
libc.my_func_wrapper( 1, 2 )
</code>


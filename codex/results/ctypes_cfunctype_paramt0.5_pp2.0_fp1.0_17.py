import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_double, ctypes.c_double)

# Define the function
@FUNTYPE
def function( x, y ):
    return x**2 + y**2

# Get the function pointer
func_pointer = FUNTYPE( function )

# Use the function pointer
print( func_pointer( 2, 3 ) )  # 13
</code>

The problem is that if I try to do this with a more complex function:
<code>from __future__ import print_function
import ctypes

# Define the function
def function( x, y ):
    return x**2 + y**2

# Define the function pointer
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_double, ctypes.c_double)
func_pointer = FUNTYPE( function )

# Use the function pointer
print( func_pointer( 2, 3 ) )  # 13
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test

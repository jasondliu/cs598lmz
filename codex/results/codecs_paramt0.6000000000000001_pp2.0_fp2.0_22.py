import codecs
codecs.register_error('strict', codecs.ignore_errors)

# If we are on a Windows machine, we will need to set some environment
# variables so that we can find the DLLs that we need
if sys.platform == 'win32':
    import os
    os.environ['PATH'] = os.environ['PATH'] + ';' + os.path.join(
        os.path.dirname(__file__), 'dlls')

# Import the appropriate modules
from ctypes import *

# Define some constants
DLL_PATH = os.path.join(os.path.dirname(__file__), 'dlls')

# Define the function prototypes
# The function prototypes tell the program what the function should
# do, but do not actually define the function.  This allows us to
# change the library that we are using without having to change the
# code.  This is an important part of creating a modular application.

# Create a new ctypes prototype for the function
# c_int defines the function argument and return types
# c_void_p defines the function argument and return types


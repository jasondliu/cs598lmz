import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER with a function returning a pointer.
# This will fail on windows because of missing 'const' keyword.
#
# The problem is that the 'const' keyword is not part of the function
# declaration, but the function definition.

from ctypes import *

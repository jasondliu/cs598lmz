import ctypes
# Test ctypes.CFUNCTYPE
#
# The code below is a modified version of code from the ctypes tutorial,
# see http://starship.python.net/crew/theller/ctypes/tutorial.html
#
# The original code was written by Thomas Heller, and is released under
# the PSF license. 
#

from ctypes import *

# Load the DLL manually to ensure that it is loaded before the test runs.
# This is a workaround for an apparent bug in Python 2.4 on Windows.
# See http://bugs.python.org/issue1628884

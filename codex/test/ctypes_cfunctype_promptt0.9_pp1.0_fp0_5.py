import ctypes
# Test ctypes.CFUNCTYPE(*extra_args)(callable)
# for docstring, where *extra_args adds up to 2 values, like
# int and c_char_p uppon the callable's arguments, in the 'argtypes' attribute.
#
# Written by Ingmar Stieger (PAP018)
#
# $Id: test_CFUNCTYPE2.py 58869 2009-12-01 12:10:22Z benjamin.peterson $
#
# Sample code: 

import _ctypes_test

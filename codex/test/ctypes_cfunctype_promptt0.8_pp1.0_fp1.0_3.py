import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a cffi port of the (rather old) "test_cfunctype.py" from CPython:
# https://github.com/python/cpython/blob/3.3/Lib/ctypes/test/test_cfunctype.py
#
# CPython's "test_cfunctype.py" is a regression test for ctypes,
# and that's what we are doing here. It was written in 2005/2006 by
# Thomas Heller <theller@ctypes.org> when ctypes was a Boost.Python-
# based project.


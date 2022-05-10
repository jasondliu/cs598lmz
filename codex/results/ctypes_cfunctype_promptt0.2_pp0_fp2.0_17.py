import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_cfunctype test.
#
# The test is run twice, once with the standard ctypes.CFUNCTYPE and
# once with the ctypes.CFUNCTYPE from the _ctypes module.
#
# The test is run with the standard ctypes.CFUNCTYPE first.
#
# The test is run with the _ctypes.CFUNCTYPE second.
#
# The _ctypes.CFUNCTYPE is used to test the ctypes module when
# the _ctypes module is compiled with the Py_LIMITED_API define.
#
# The _ctypes.CFUNCTYPE is used to test the _ctypes module when
# the _ctypes module is compiled without the Py_LIMITED_API define.
#
# The _ctypes.CFUNCTYPE is used to test the _ctypes module when
# the _ctypes module is compiled with the Py_LIMITED_API define
# and the Py_BUILD_CORE define.
#


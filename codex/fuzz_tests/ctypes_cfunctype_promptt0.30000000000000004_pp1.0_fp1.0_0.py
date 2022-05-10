import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test/cfunctype.py test in the Python source
# distribution.
#
# The test is run with the following command line:
#
#   python test/cfunctype.py
#
# The test should produce no output.

# Check that the test is being run with the correct version of Python.

import sys
if sys.version_info[:2] != (2, 7):
    raise Exception("This test must be run with Python 2.7")

# Check that ctypes is available.

try:
    import ctypes
except ImportError:
    raise Exception("This test requires the ctypes module")

# Check that ctypes.CFUNCTYPE is available.

try:
    ctypes.CFUNCTYPE
except AttributeError:
    raise Exception("This test requires the ctypes.CFUNCTYPE function")

# Check that ctypes.pythonapi is available.

try:
    ctypes.pythonapi
except AttributeError:
    raise Exception("This test requires the ctypes.python

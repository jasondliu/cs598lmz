import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not run automatically, but must be run manually.
#
# The test is meant to be run from the command line with a command like:
#
#   python test_cfunctype.py
#
# The test should print "OK" and exit with status 0.
#
# The test is not run automatically because it requires manual intervention.
#
# The test creates a C function that calls back into Python.  The Python
# callback is a CFUNCTYPE.  The C function is called, and the callback
# is called.  The callback is expected to return a value to the C function,
# which is returned to the Python caller.
#
# The test is successful if the returned value is the same as the value
# passed to the callback.
#
# The test is not run automatically because it requires that a C compiler
# be installed.  The test creates a C source file, compiles it, and runs
# the resulting executable.
#
# The test is not run automatically because it's not clear how to do
# the manual intervention in an automated way.  The test creates a C

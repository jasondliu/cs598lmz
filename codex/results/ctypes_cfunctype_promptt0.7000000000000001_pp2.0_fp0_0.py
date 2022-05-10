import ctypes
# Test ctypes.CFUNCTYPE
ctypes.CFUNCTYPE(ctypes.c_int)

# This program does not crash

# Problem is: http://bugs.python.org/issue23042


# After running the program, the following file is created:
#
# /tmp/python_crash_test_14356
#
# Delete this file to run the program again.
#
# When running the program, the following message is displayed:
#
# Error in sys.excepthook:
#
# Original exception was:
#
#
# Process finished with exit code 0

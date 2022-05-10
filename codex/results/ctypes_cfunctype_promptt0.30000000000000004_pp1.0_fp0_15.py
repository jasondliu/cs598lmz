import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test for a bug in ctypes.CFUNCTYPE.  The bug is that the
# CFUNCTYPE object would not be properly garbage collected if the
# function object it created was still alive.  This test creates a
# CFUNCTYPE object, and then creates a function object from it.  It
# then deletes the CFUNCTYPE object, and checks to see if the function
# object can still be called.
#
# This test is run with a number of iterations, and the number of
# iterations is passed in as the first argument.  The default number of
# iterations is 100.
#
# This test was written by Thomas Heller.

# This is the number of iterations to run.
num_iterations = 100

# This is the number of iterations to run.
if len(sys.argv) > 1:
    num_iterations = int(sys.argv[1])

# This is the function that we will call.
def func(x):
    return x

# This is the type of the function that we will call.


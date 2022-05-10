import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.enable()/gc.disable()

# This test is intended to be run by regrtest.py.
#
# It needs to make it easy to check that its test cases are doing the right
# thing.  It uses the following approach:
#
#   - The test cases are in functions that are called by the run() function.
#   - Each test case sets global variables to indicate which case it is.
#     These variables are then used by the run() function to check that
#     the test case did the right thing.

# List of test cases.
# Each list item is a tuple containing:
#   - a string used to display the test name
#   - a function object for the test case
#   - a tuple containing the expected arguments to the callbacks

# The callbacks will be called with the objects in this list as their
# argument.
objects = [42, ('hello', 'world'), {}]

# The callbacks will be called with the objects in this list as their
# keyword arguments.
keywords = [('answer', 42), ('greeting', 'hello'),

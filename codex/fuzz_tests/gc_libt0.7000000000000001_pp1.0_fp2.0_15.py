import gc, weakref
import sys

# todo:
# - add a 'load(filename)' method, which reads a pickle, and
#   re-constructs the exact object?
#   - this can be done, but it needs to be determined when
#     to execute the code.  (after all the classes are defined?)
# - watch out for reference cycles (can this happen?)
# - don't execute code that is being executed?
# - what if a class has no __init__ method?
# - there are probably some other problems...
#
# - watch out for circular dependencies in the code.
#
# - take care of "import *" statements
#

# --------------------------------------------------------
# The code below is based on Python 2.2.2 (the latest
# version as of this writing)

# This is some code to help with pickling objects.
# You must inherit from the classes defined here,
# and you need to use the Pickler class to pickle
# the objects.
#
# This is all pretty experimental, and might not work
# for you.
#
# The pickler doesn't know about classes

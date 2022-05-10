import types
types.MethodType(lambda self: None, None, None)

# This is a regression test for a bug in the Python 2.5.1
# implementation of __new__ on new-style classes.
#
# The bug was that the __new__ method of a new-style class
# was not being called when the class was subclassed.
#
# The bug was fixed in Python 2.5.2.

class A(object):
    def __new__(cls, *args, **kwargs):
        return super(A, cls).__new__(cls)

class B(A):
    pass

B()

# This is a regression test for a bug in the Python 2.5.1
# implementation of __new__ on new-style classes.

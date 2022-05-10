fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it raises a SystemError.
# The problem is that the code object is not a code object, but a
# generator.  The code object is not checked until the function is
# called.  The problem is that the code object is not a code object,
# but a generator.  The code object is not checked until the function
# is called.  The problem is that the code object is not a code
# object, but a generator.  The code object is not checked until the
# function is called.  The problem is that the code object is not a
# code object, but a generator.  The code object is not checked until
# the function is called.  The problem is that the code object is not
# a code object, but a generator.  The code object is not checked
# until the function is called.  The problem is that the code object
# is not a code object, but a generator.  The code object is not
# checked until the function is called.  The problem is that the code
# object is not a code object, but a generator. 

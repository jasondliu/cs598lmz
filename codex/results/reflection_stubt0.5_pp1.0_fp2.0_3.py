fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError as e:
    print(e)

# TypeError: 'generator' object is not callable


# __code__ attribute can be set to any object.
# But it has to be an object with the attributes
# co_code, co_filename, co_firstlineno, co_name,
# co_nlocals, co_stacksize, co_varnames, and co_argcount.
# These attributes are used by the interpreter.
# If any of these attributes is missing,
# the interpreter will raise an exception.
# This is the reason why we get the TypeError.

# We can also use a generator as a code object.
# A generator is an object with a __next__ method.
# The __next__ method is called by the interpreter
# to execute the next statement of the code object.
# Note that we are not invoking the __next__ method
# directly. The interpreter will do that for us.

# In the example, we define a generator that returns the
# next statement of the code object.
# The

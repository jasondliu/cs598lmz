fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Code objects are not callable, so we pass in a generator
# instead.  We do have to make it look like a code object, though.
"""
call_code_fn = """
def call_code_fn():
    a = lambda: None
    a.__code__ = a
    return a()
"""

# The code object returned by the second generator expression doesn't
# have any fields set.  The function object's __code__ is set to None
# and the function is called.
"""
call_none_fn = """
def call_none_fn():
    a = lambda: None
    a.__code__ = None
    return a()
"""

# The code object returned by the generator expression has some
# fields set to invalid values.  The function object's __code__ is set
# to the code object and the function is called.
"""
call_code_fn_invalid = """
def call_code_fn_invalid():
    a = lambda: None
    a.__code__ = a
    a.__code__.co_argcount

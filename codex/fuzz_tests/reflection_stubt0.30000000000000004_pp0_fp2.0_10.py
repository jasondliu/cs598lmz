fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following is a regression test for a bug in the
# implementation of the __code__ attribute.  The bug was
# that the reference count of a code object was not
# incremented when it was assigned to the __code__
# attribute of a function object.  This caused the code
# object to be freed too early.

# The bug was triggered by the following code, which
# created a function object, assigned a code object to
# its __code__ attribute, and then deleted the function
# object.  The code object was freed too early, and the
# next time a code object was allocated, it was allocated
# at the same address as the freed code object.  The
# following then caused a segfault.

import types

def f(): pass

def g():
    f.__code__ = types.FunctionType(f.__code__.co_code,
                                    f.__code__.co_globals,
                                    'g',
                                    f.__code__.co_defaults,
                                    f.__code__.co_

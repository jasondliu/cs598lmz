fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise TypeError:
# "code object passed to exec() may not contain free variables"

# This is a regression test for SF bug #1080163.
# The bug was that the code object was being created with
# the wrong size, so a segfault occurred when the code object
# was executed.

# The bug was fixed by changing the code in ceval.c to use
# PyCode_NewEmpty() instead of PyCode_New() to create the
# code object.

# This test was written by Andrew Kuchling.

# The test is disabled because it's not clear what the correct
# behavior should be.  The code object is created with the wrong
# size, but it's not clear that this is a problem.  The code
# object is created with a size of 0, which means that it's
# treated as if it has no local variables.  This is probably
# the correct behavior.

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# This is a regression test for a bug in the Python 2.7.3
# implementation of the inspect module.  The bug was that
# isgeneratorfunction() did not check the type of the code
# object passed to it, and so gave a spurious True result
# if passed a code object belonging to a generator iterator.

# The bug was fixed in Python 2.7.4 by adding a type check
# for code objects.


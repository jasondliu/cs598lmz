fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# and this one with the same thing, but using a function instead of a lambda
def g():
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
    fn()

g()

# this one tells the version of python
import sys
print(sys.version)

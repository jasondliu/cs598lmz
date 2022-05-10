fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn()

# Issue #22386: Ensure that the __code__ attribute of a function is
# writable.
def f():
    pass
f.__code__ = type(f.__code__)()

# Issue #22386: Ensure that the __code__ attribute of a method is
# writable.
class C(object):
    def m(self):
        pass
C.m.__code__ = type(C.m.__code__)()

# Issue #22386: Ensure that the __code__ attribute of a built-in
# function is writable.
import sys
sys.__code__ = type(sys.__code__)()

# Issue #22386: Ensure that the __code__ attribute of a built-in
# method is writable.
import sys
sys.exit.__code__ = type(sys.exit.__code__)()

# Issue #22386: Ensure that the __code__ attribute of a built-in
# method wrapper is writable.
import sys
sys

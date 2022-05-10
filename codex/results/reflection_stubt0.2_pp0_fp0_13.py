fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22983: Ensure that the __code__ attribute of a built-in function
# is not replaced by a user-defined object.
import sys
def f():
    pass
f.__code__ = sys.getrefcount
f()

# Issue #23018: Ensure that the __code__ attribute of a built-in function
# is not replaced by a user-defined object.
import sys
def f():
    pass
f.__code__ = sys.getrefcount
f()

# Issue #23019: Ensure that the __code__ attribute of a built-in function
# is not replaced by a user-defined object.
import sys
def f():
    pass
f.__code__ = sys.getrefcount
f()

# Issue #23020: Ensure that the __code__ attribute of a built-in function
# is not replaced by a user-defined object.
import sys
def f():
    pass
f.__code__ = sys.getrefcount
f()

# Issue #23021: Ensure that the __code__ attribute of a

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of an instance
# is read-only.
class C: pass
c = C()
c.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of a class
# is read-only.
C.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of a module
# is read-only.
import sys
sys.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of a function
# is read-only.
def f(): pass
f.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of a method
# is read-only.
class C:
    def m(self): pass
c = C()
c.m.__code__ = gi

# Issue #23481: make sure that the __code__ attribute of a builtin
# is read-only.
import sys
sys.exit.__code__ = gi

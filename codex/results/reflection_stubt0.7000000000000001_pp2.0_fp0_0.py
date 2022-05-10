fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_names

# Issue #20553: Crash when running pydoc on __builtin__.__import__()
import pydoc
pydoc.render_doc(__import__)

# Issue #12356: Crash when running pydoc on __import__
import pydoc
pydoc.render_doc(__builtin__.__import__)

# Issue #12356: Crash when running pydoc on __import__
import pydoc
pydoc.render_doc(__builtins__.__import__)

# Issue #20558: Crash when running pydoc on a class method
class A:
    def foo(cls):
        return cls
A.foo = classmethod(A.foo)
import pydoc
pydoc.render_doc(A.foo)

# Issue #20559: Crash when running pydoc on a staticmethod
class A:
    def foo():
        pass
A.foo = staticmethod(A.foo)
import pydoc
pyd

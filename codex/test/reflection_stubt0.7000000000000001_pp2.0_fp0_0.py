fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_names

# Issue #20553: Crash when running pydoc on __builtin__.__import__()
import pydoc
pydoc.render_doc(__import__)

# Issue #12356: Crash when running pydoc on __import__
import pydoc

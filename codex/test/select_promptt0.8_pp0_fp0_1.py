import select
# Test select.select
from select import select
r, w, e = select([], [], [], 0.1)
assert r == w == e == [], "select failed"
# Test select.__doc__
from test_support import verbose
if verbose:
    import select
    doc = select.__doc__

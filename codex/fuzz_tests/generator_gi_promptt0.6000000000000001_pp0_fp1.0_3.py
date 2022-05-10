gi = (i for i in ())
# Test gi.gi_code is not None
assert next(gi).gi_code is not None

# Test gi_frame is not None (see also bpo-27707)
gi = (i for i in ())
assert next(gi).gi_frame is not None

# Test gi_running is 0
def bar():
    gi = (i for i in ())
    return next(gi).gi_running
assert bar() == 0

# Test gi_yieldfrom is None
gi = (i for i in ())
assert next(gi).gi_yieldfrom is None

# Test gi_running is 1
def foo():
    gi = (i for i in ())
    next(gi)
    return gi.gi_running
assert foo() == 1

# Test gi_running is 0
def foo():
    gi = (i for i in ())
    next(gi)
    next(gi)
    return gi.gi_running
assert foo() == 0

# Test gi_yieldfrom is None
def foo():
    gi = (i for i in

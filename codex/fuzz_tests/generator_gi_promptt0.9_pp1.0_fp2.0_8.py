gi = (i for i in ())
# Test gi.gi_code.co_name is set correctly.
name = gi.gi_code.co_name
# Test sequence get
vi = tuple(gi)[0]

# Test properties of StopIteration
si = StopIteration()
si.value
si.value = 0
si.args
si.args = (0,)

# Test next(i)
next(gi)

# Test StopIteration handling
try:
    next(gi)
except StopIteration as e:
    assert e.value is None
    # Check args? XXX
    pass
else:
    assert False

gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None
# Test gi.gi_frame
assert gi.gi_frame is None
# Test gi.gi_running
assert gi.gi_running is False
# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.send()
try:
    gi.send(None)
except StopIteration:
    pass
else:
    assert False, "send() on empty generator should raise StopIteration"

# Test gi.throw()
try:
    gi.throw(RuntimeError)
except RuntimeError:
    pass
else:
    assert False, "throw() on empty generator should raise RuntimeError"

# Test gi.close()
gi.close()

# Test gi.send()
try:
    gi.send(None)
except StopIteration:
    pass
else:
    assert False, "send() on closed generator should raise StopIteration"

# Test gi.throw()
try:
    gi.throw(RuntimeError

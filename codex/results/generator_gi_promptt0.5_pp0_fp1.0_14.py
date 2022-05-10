gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 0x4
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test .close()
gi = (i for i in ())
gi.close()
try:
    next(gi)
except StopIteration:
    pass
else:
    raise AssertionError("gi.close() did not close the generator")

# Test .throw()
gi = (i for i in ())
try:
    gi.throw(RuntimeError)
except RuntimeError:
    pass
else:
    raise AssertionError("gi.throw() did not raise RuntimeError")

# Test .send()
gi = (i for i in ())
try:
    gi.send(None)
except StopIteration:
    pass
else:
    raise AssertionError("gi.send(None) did not raise StopIteration")

# Test .gi_running
gi = (i for i in ())
assert gi.gi_running is

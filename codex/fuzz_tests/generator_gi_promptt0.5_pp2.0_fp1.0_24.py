gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
assert gi.gi_code is None and gi.gi_frame is None

# Test gi.gi_running
assert not gi.gi_running

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.send
try:
    gi.send(42)
except TypeError:
    pass
else:
    assert False, "should not be able to send to a generatoriterator"

# Test gi.throw
try:
    gi.throw(ZeroDivisionError)
except TypeError:
    pass
else:
    assert False, "should not be able to throw to a generatoriterator"

# Test gi.close
gi.close()
assert True, "close() should not raise an exception"

# Test gi.gi_frame
gi = (i for i in range(5))
gi.gi_frame.f_locals

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti == -

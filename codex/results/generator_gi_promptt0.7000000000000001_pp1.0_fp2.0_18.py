gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom

# Test send()
gi.send(None)
gi.send(1)
gi.send(2)
try:
    gi.send(3)
except StopIteration as e:
    assert e.value == 2
else:
    assert False

# Test throw()
gi = (i for i in range(3))
try:
    gi.throw(ValueError)
except ValueError:
    pass
else:
    assert False
try:
    gi.throw(ValueError)
except ValueError:
    pass
else:
    assert False
try:
    gi.throw(ValueError)
except ValueError:
    pass
else:
    assert False
try:
    gi.throw(ValueError)
except StopIteration:
    pass
else:
    assert False

# Test close()
gi = (i for i in range(3))
try:
    gi.close()
except ValueError:

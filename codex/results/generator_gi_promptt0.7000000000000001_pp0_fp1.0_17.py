gi = (i for i in ())
# Test gi.gi_code
gi_code = gi.gi_code
# Test gi.gi_frame
gi_frame = gi.gi_frame
# Test gi.gi_running
gi_running = gi.gi_running
# Test gi.gi_yieldfrom
gi_yieldfrom = gi.gi_yieldfrom

# Test gi.send(value)
try:
    gi.send(5)
except StopIteration as e:
    assert e.value == 6
else:
    raise Exception("Did not raise StopIteration")

# Test gi.throw(exc)
try:
    gi.throw(ValueError("Error"))
except ValueError as e:
    assert e.args[0] == "Error"

# Test gi.close()
gi.close()

# Test gi.send(value)
try:
    gi.send(5)
except StopIteration as e:
    assert e.value == 6
else:
    raise Exception("Did not raise StopIteration")

# Test gi.throw(exc

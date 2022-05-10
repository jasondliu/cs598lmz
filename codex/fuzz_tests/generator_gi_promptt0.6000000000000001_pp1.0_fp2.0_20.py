gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None
# Test gi.gi_frame
assert gi.gi_frame is None
# Test gi.gi_running
assert gi.gi_running is False
# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None
# Test gi.__name__
assert gi.__name__ == ""
# Test gi.__qualname__
assert gi.__qualname__ == ""
# Test gi.__annotations__
assert gi.__annotations__ == {}
# Test gi.__kwdefaults__
assert gi.__kwdefaults__ == None
# Test gi.__defaults__
assert gi.__defaults__ == None
# Test gi.__code__
assert gi.__code__ is None
# Test gi.__globals__
assert gi.__globals__ is None
# Test gi.__dict__
assert gi.__dict__ == {}
# Test gi.__closure__
assert gi.__closure__ ==

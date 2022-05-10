gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)
# Test gi.__name__ is None
print(gi.__name__)
# Test gi.__qualname__ is None
print(gi.__qualname__)
# Test gi.__module__ is None
print(gi.__module__)
# Test gi.__annotations__ is {}
print(gi.__annotations__)
# Test gi.__kwdefaults__ is None
print(gi.__kwdefaults__)
# Test gi.__defaults__ is None
print(gi.__defaults__)
# Test gi.__closure__ is None
print(gi.__closure__)
# Test gi.__code__.co_name is ''
print(gi.__code__.co_name)
#

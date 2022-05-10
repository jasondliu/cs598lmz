gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_running and gi.gi_name.
gi.gi_code = None
gi.gi_frame = None
gi.gi_running = True
gi.gi_name = None
gi.gi_callee = None
gi.gi_qualname = None
# Test str(ci), repr(ci),
print(str(gi))
print(repr(gi))
# Test bool(ci)
print(bool(gi))
# Test constructor
print(functools.partial(bool))
print(functools.partial(bool, 1))
# Test function attributes
print(functools.partial(bool).__name__)
print(functools.partial(bool).__module__)
print(functools.partial(bool).__defaults__)
print(functools.partial(bool).__kwdefaults__)
print(functools.partial(bool).__code__)
print(functools.partial(bool).__dict__)
print(functools.partial(bool).__closure__)


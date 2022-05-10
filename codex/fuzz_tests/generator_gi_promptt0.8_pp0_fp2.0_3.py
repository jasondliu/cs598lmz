gi = (i for i in ())
# Test gi.gi_code is a function
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi has no method gi_frame
# print(dir(gi))
# Test will fail without PYTHONFRAMEOBJECT defined.
# print(gi.gi_frame)

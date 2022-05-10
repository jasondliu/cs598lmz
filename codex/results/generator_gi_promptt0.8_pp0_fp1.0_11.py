gi = (i for i in ())
# Test gi.gi_code:
print(gi.gi_code)
print(gi.gi_code.co_code)
print()
# Test gi.gi_frame:
print(gi.gi_frame)
print(gi.gi_frame.f_code)
print(gi.gi_frame.f_code.co_code)
# The .co_code attribute is not a string as in Python 2.7, but a bytes object.
print(gi.gi_frame.f_code.co_code.__class__)

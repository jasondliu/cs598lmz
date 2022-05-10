gi = (i for i in ())
# Test gi.gi_code.
try:
    gi.__code__
except AttributeError:
    pass
else:
    print("FAILED: generator __code__ works on sentinel")
gi = (i for i in ())
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("FAILED: generator gi_code works on sentinel")
gi = (i for i in ())
try:
    gi.gi_frame
except ValueError:
    pass
else:
    print("FAILED: generator gi_frame works on sentinel")
# The frame will be cleaned up even when the generator isn't closed,
# so be careful when looking at the frame object.
gi = (i for i in (1, 2, 3))
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_locals)

gi.__next__()
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_locals)

gi.__next__()

gi = (i for i in ())
# Test gi.gi_code on a generator-iterator.
assert gi.gi_code is g.__code__
# Test gi.gi_frame on a generator-iterator.
assert isinstance(gi.gi_frame, types.FrameType)
assert gi.gi_frame.f_code is g.__code__
assert gi.gi_frame.f_lasti == -1
assert gi.gi_frame.f_locals is g.__closure__[0].cell_contents

# Test gi.gi_frame.f_trace on a generator-iterator.
# XXX: What should this return?  Not implementedError for now.
try:
    gi.gi_frame.f_trace
except NotImplementedError:
    pass
else:
    raise Exception("expected NotImplementError")

# Test gi.gi_frame.f_trace_lines on a generator-iterator.
# XXX: What should this return?  Not implementedError for now.
try:
    gi.gi_frame.f_trace_lines
except NotImplementedError:
    pass
else

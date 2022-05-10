gi = (i for i in ())
# Test gi.gi_code.co_flags
print('gi_code.co_flags is', hex(gi.gi_code.co_flags))
# Test gi.gi_code.co_flags is generator
print('gi_code.co_flags is generator?',
      bool(gi.gi_code.co_flags & gen.CO_GENERATOR))
# Test gi.gi_frame is None
print('gi.gi_frame is None?', gi.gi_frame is None)

# Make an empty list as generator argument
tgi = (i for i in [])
# Test tgi.gi_code.co_flags
print('tgi_code.co_flags is', hex(tgi.gi_code.co_flags))
# Test tgi.gi_code.co_flags is generator
print('tgi_code.co_flags is generator?',
      bool(tgi.gi_code.co_flags & gen.CO_GENERATOR))
# Test tgi.gi_frame is not None
print('tgi.gi_frame is not None?', tgi.gi_

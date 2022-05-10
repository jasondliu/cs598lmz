gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_code.co_filename)
print(gi.gi_code.co_name)
print(gi.gi_code.co_firstlineno)
print(gi.gi_code.co_flags & CODE_FLAGS_MASK)
print(gi.gi_frame.f_back)

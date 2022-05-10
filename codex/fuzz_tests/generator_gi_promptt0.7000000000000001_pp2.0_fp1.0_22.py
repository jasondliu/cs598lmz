gi = (i for i in ())
# Test gi.gi_code.co_filename.  Also tests gi.gi_frame.f_code.co_filename.
try:
    gi.gi_code.co_filename
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_code.co_filename)
print(gi.gi_frame.f_code.co_filename)

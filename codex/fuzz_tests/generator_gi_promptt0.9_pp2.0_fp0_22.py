gi = (i for i in ())
# Test gi.gi_code.co_filename.
assert gi.gi_code.co_filename == 'empty_genexpr'

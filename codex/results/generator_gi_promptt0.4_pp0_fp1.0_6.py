gi = (i for i in ())
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ('i',)
# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {'i': 0}

# Test gi.gi_frame.f_locals
gi.send(1)
assert gi.gi_frame.f_locals == {'i': 1}

# Test gi.gi_frame.f_locals
gi.send(2)
assert gi.gi_frame.f_locals == {'i': 2}

# Test gi.gi_frame.f_locals
gi.send(3)
assert gi.gi_frame.f_locals == {'i': 3}

# Test gi.gi_frame.f_locals
gi.send(4)
assert gi.gi_frame.f_locals == {'i': 4}

# Test gi.gi_frame.f_locals
gi.send(5)
assert gi.gi

gi = (i for i in ())
# Test gi.gi_code

A = type('A', (object,), {'__iter__': gi})

A().__iter__()

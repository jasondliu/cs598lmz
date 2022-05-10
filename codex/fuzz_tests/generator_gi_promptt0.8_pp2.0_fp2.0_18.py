gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code
# Test gi.gi_frame is None
gi.gi_frame


# SF #1475559: the repr() of a generator is not informative.
#
# Check that repr() returns "<generator object <genexpr> at 0x...>".
# Also check that the generated code attribute is set.
gi = (i for i in ())
'<generator object %s at %#x>' % (gi.gi_code.co_name, id(gi))

gi = ((x,y) for x in range(2) for y in range(3))
'<generator object %s at %#x>' % (gi.gi_code.co_name, id(gi))

def g():
    yield 1
    yield 2
    yield 3

gi = g()
'<generator object %s at %#x>' % (gi.gi_code.co_name, id(gi))

# SF bug #1263: local variable lookup in genexp
def g(m=[]):
    z = (f() for

gi = (i for i in ())
# Test gi.gi_code.co_code
# ...
#
# This fails under Python 2.4, because gi.gi_code.co_code is still
# the bytecode for gi, when it should have been replaced by an empty
# bytecode.

def get_gi():
    return (i for i in ())
gi = get_gi()
code = gi.gi_code.co_code
gi.gi_code.co_code = ""
gi.gi_code.co_code
code
gi.gi_code.co_code == code
# Test that gi_code is actually written back to the generator, so that
# we don't lose it when the generator is destroyed.
gi.gi_code.co_code = ""
gi = get_gi()
gi.gi_code.co_code == ""

# Test behavior of generators in with statements.

def g():
    v.append(1)
    yield
    v.append(3)
with g() as gg:
    v.append(2)
v

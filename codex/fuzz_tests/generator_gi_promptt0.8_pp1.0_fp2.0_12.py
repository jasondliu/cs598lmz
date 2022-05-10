gi = (i for i in ())
# Test gi.gi_code == None, i.e. iterator doesn't have __code__ attribute
assert_equal(gi.gi_code, None)
# test iterator.gi_frame is None, i.e. iterator doesn't have __frame__ attribute
assert_equal(gi.gi_frame, None)

# test generator has __code__ and __frame__ attributes
# use a generator which doesn't yield
def gen():
    return 1

# NOTE: code.co_flags & CO_GENERATOR is not reliable way to detect generator
# object because it could be a generator function or a generator iterator
# object.
#
# Here it is possible to construct generator object by passing a generator
# function object to `type.__call__`
g = type(gen)(gen)
assert_equal(g.gi_code.co_flags & CO_GENERATOR == CO_GENERATOR, True)

# The generator object has a `gi_code` attribute which is a code object.
assert_equal(g.gi_code.co_name, 'gen')
assert_equal(g.gi_code.co_filename,

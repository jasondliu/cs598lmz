gi = (i for i in ())
# Test gi.gi_code.co_flags contains CO_FUTURE_GENERATOR_STOP
set_flag(type(gi).__flags__, CO_FUTURE_GENERATOR_STOP)

# Generate a generator (g1) using gi.__next__()
g1 = gi.__next__()
# Ensure g1 has type Generator
assert isinstance(g1, Generator), 'g1 is not a Generator'
# Ensure g1.gi_future has type Future
assert isinstance(g1.gi_future, Future), 'g1.gi_future is not a Future'
# Ensure g1.gi_yieldfrom is None
assert g1.gi_yieldfrom is None, 'g1.gi_yieldfrom is not None'

# Invoke g1.send(None) - should swap out the generator iterator gi
# to invoke the inner 'while True' loop in the generator
v = g1.send(None)
# Ensure the returned value is 42
assert v == 42, 'g1.send(None) returned an unexpected value %r' % (v,)


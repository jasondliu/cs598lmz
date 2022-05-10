gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
test_call(gi)
# Test gi.gi_code.co_varnames
test_call(gi, 'x')
test_call(gi, 'x', 2)
test_call(gi, x=2)
test_call(gi, 'x', x=2)
test_call(gi, 'x', y=2)

# Test with a many-arguments generator
def gen():
    yield 1
    yield 2
    yield 3

gi = gen()
# Test gi.gi_code.co_argcount
test_call(gi, 1)
test_call(gi, 1, 2)
test_call(gi, 1, 2, 3)
# Test gi.gi_code.co_firstlineno
test_call(gi, 1)
test_call(gi, 1, 2)
test_call(gi, 1, 2, 3)
# Test gi.gi_code.co_varnames
test_call(gi, 1, 'x')
test_call(gi, 1, 2,

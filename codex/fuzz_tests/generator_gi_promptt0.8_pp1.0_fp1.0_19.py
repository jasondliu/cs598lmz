gi = (i for i in ())
# Test gi.gi_code is NULL
test_support.check_code_unreachable(gi.gi_code)

# Test empty generator that immediately raises StopIteration
def f():
    yield
assert_raises(StopIteration, next, f())

# Test generator that yields one value
def g():
    yield 1
gi = g()
assert_equals(gi.gi_code.co_flags & CO_GENERATOR, CO_GENERATOR)
assert_equals(gi.gi_frame.f_back, None)
assert_equals(gi.gi_frame.f_lasti, -1)
assert_equals(gi.gi_frame.f_locals, gi.gi_frame.f_globals)
assert_equals(gi.gi_frame.f_locals, gi.gi_frame.f_builtins)
assert_equals(gi.gi_frame.f_lasti, -1)
assert_equals(next(gi), 1)
assert_equals(gi.gi_frame.f_lasti, 4)
assert_

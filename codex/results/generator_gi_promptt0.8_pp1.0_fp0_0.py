gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_name == '<module>'

# Test __repr__ for generator
gi = (i for i in ())
assert repr(gi) == '<generator object <genexpr> at 0x%x>' % id(gi)

# Test generator.gi_yieldfrom
def yielded_generator():
    yield 1
    yield 2

def yield_from_generator():
    yield 0
    yield from yielded_generator()
    yield 3

assert list(yield_from_generator()) == [0, 1, 2, 3]

# Test tuple unpacking on return
def p(a):
    return a, 42

# Test a yield expression
def generator():
    yield 42

def caller():
    yield from generator()

assert next(caller()) == 42

# Test a yield from expression with a non-iterable
def caller():
    yield from 1

with py

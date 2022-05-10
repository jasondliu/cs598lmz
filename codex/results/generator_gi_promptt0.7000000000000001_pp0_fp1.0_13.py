gi = (i for i in ())
# Test gi.gi_code is None
assert gi.gi_code is None
# Test gi.gi_frame is None
assert gi.gi_frame is None
# Test gi.gi_running is 0
assert gi.gi_running == 0
# Test gi.gi_yieldfrom is None
assert gi.gi_yieldfrom is None

# Test __next__
assert [i for i in gi] == []

# Test throw
try:
    gi.throw(TypeError, 'Error')
    raise Exception('Should have raised')
except TypeError as e:
    assert str(e) == 'Error'

def gen():
    yield 1
    yield 2
    yield 3

# Test gi_code
gi = gen()
assert gi.gi_code.co_filename == __file__

# Test gi_frame
assert gi.gi_frame.f_locals == {
    'gen': gen,
    'gi': gi,
    '__name__': '__main__',
    '__doc__': None,
    '__

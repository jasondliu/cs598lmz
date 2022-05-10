gi = (i for i in ())
# Test gi.gi_code is OK.
gi.gi_code
# Test gi.gi_frame is None.
gi.gi_frame is None
# Test gi.gi_running is false.
gi.gi_running is False
# Test gi.gi_yieldfrom is None.
gi.gi_yieldfrom is None

# Test the attributes for a generator.
# XXX: I don't know how to test for the frame, frame.f_lasti and frame.f_lineno
# attributes.
def gen():
    yieldfrom range(5)
gen = gen()
gen.gi_code
gen.gi_frame is not None
gen.gi_running is False
gen.gi_yieldfrom is None

# Test that __await__ is called on __iter__ if it exists.
class Iterator:
    def __iter__(self):
        # The call to __await__ here should not fail.
        await (yield 1)
        yield 2

i = Iterator()
for j in i:
    assert j == 1
del j

# Test that __await

gi = (i for i in ())
# Test gi.gi_code

# gi.gi_frame can be tested with a yield, then I would have to make all the frames, so skip

# Test gi.gi_running
# gi.gi_running should start as False then after yield it should be True
a = gi.gi_running
yield
b = gi.gi_running
print(a, b)
# Test gi.gi_yieldfrom
# gi.gi_yieldfrom should be None until the generator is passed to another generator, then it shoud be the 
# generator whose method is being executed
gi = (i for i in ())
print(gi.gi_yieldfrom)
def do_yield(gi):
    yield from gi
do_yield(gi)
print(gi.gi_yieldfrom)
# Test gi.gi_name
a = (i for i in ())
print(a.gi_name)
# Test gi.gi_qualname
# gi.gi_qualname should be the uname
def do_yield(gi):
    yield from gi
a

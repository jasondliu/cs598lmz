gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
assert gi.gi_code is None
assert gi.gi_frame is None
# Test gi.gi_running
# Test gi.gi_yieldfrom
assert gi.gi_running is False
assert gi.gi_yieldfrom is None
# Test gi.__name__
assert gi.__name__ == 'i'
# Test gi.__qualname__
assert gi.__qualname__ == 'i'
try:
    next(gi)
except StopIteration:
    pass

# Test genexp's gi_frame and gi_running
# Bug #26898
def inner():
    for i in ():
        yield i

def outer(i):
    return i

def bar():
    return outer(inner())

gen = bar()
gi = gen.gi_frame
assert gi.f_code.co_name == "inner"
assert gi.f_back.f_code.co_name == "outer"
assert gi.f_back.f_back

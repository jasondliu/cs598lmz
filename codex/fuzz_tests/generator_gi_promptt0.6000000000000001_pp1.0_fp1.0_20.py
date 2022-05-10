gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.__name__
gi.__name__
# Test gi.__qualname__
gi.__qualname__
# Test gi.__next__
gi.__next__()
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(TypeError)
# Test gi.close
gi.close()

# Test lgi.__length_hint__
gi.__length_hint__()

# Test generator.gi_code
def gen():
    yield 1
g = gen()
g.gi_code

# Test generator.gi_frame
def gen():
    yield 2
g = gen()
g.gi_frame

# Test generator.gi_running
def gen():
    yield 3
g = gen()
g.gi_running

# Test

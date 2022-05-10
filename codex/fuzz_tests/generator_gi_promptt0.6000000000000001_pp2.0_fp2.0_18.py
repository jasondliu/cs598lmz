gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running

def test():
    a = 1
    yield a
    a = 2
    yield a
    a = 3
    yield a

# Test gi.gi_running
gi = test()
gi.gi_running
next(gi)
gi.gi_running
next(gi)
gi.gi_running
next(gi)
gi.gi_running

# Test gi.gi_frame
gi = test()
gi.gi_frame
next(gi)
gi.gi_frame
next(gi)
gi.gi_frame
next(gi)
gi.gi_frame

# Test gi.gi_code
gi = test()
gi.gi_code
next(gi)
gi.gi_code
next(gi)
gi.gi_code
next(gi)
gi.gi_code

# Test gi.gi_frame
gi = (i for i in ())
gi.gi_frame

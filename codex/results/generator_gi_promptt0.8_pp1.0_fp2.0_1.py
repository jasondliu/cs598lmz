gi = (i for i in ())
# Test gi.gi_code
gi_code = gi.gi_code

# Test gi.gi_frame
gi_frame = gi.gi_frame

# Test gi.gi_running
gi_running = gi.gi_running

# Test gi.gi_yieldfrom
# looks like you need to do this in py3.3, because a gen is a gi.
# see test_generator_gi
def gi_yieldfrom(): yield from ()
gi = gi_yieldfrom()
gi_yieldfrom = gi.gi_yieldfrom

# Test gi.gi_name
def gi_name(): yield from ()
gi = gi_name()
gi_name = gi.gi_name

# Test gi.gi_frame
def gi_frame(): yield from ()
gi = gi_frame()
gi_frame = gi.gi_frame


# Test gi.gi_running
def gi_running(): yield from ()
gi = gi_running()
gi_running = gi.gi_running


# Test

gi = (i for i in ())
# Test gi.gi_code.co_flags
try:
    gi.gi_code.co_flags
except AttributeError:
    pass
else:
    print('AttributeError expected')
gi.gi_code = 'hello'
gi.gi_code
gi.gi_code = ('a', 'b', 'c')
gi.gi_code
gi.gi_frame
gi.gi_frame = 'hello'
gi.gi_frame
gi.gi_frame = ('a', 'b', 'c')
gi.gi_frame
gi.gi_running
gi.gi_running = 'hello'
gi.gi_running
gi.gi_running = ('a', 'b', 'c')
gi.gi_running
gi.gi_yieldfrom
gi.gi_yieldfrom = 'hello'
gi.gi_yieldfrom
gi.gi_yieldfrom = ('a', 'b', 'c')
gi.gi_yieldfrom
# Ensure that generators expose their gi_code as __code__
class C(object):
    def __init__(self, i):
        self.

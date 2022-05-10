gi = (i for i in ())
# Test gi.gi_code is not None
print('gi.gi_code is {}'.format(gi.gi_code))
print('gi.gi_frame is {}'.format(gi.gi_frame))
print('gi.gi_running is {}'.format(gi.gi_running))
print('gi.gi_yieldfrom is {}'.format(gi.gi_yieldfrom))

# Test gi.gi_running and gi.gi_frame
def f():
    gi = (i for i in ())
    print('gi.gi_running is {}'.format(gi.gi_running))
    print('gi.gi_frame is {}'.format(gi.gi_frame))

f()

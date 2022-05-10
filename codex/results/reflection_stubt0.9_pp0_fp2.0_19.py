fn = lambda: None
gi = (i for i in ())
fn.__code__ = lambda : None
gi.gi_code = fn
gi.gi_code = 1
gi.gi_code = None
gi.gi_code = 'a'
gi.gi_code = (1, 2, 3)
gi.gi_code = [1, 2, 3]
gi.gi_code = object()

gi.gi_frame = object()
gi.gi_frame = lambda : None
gi.gi_frame = (1, 2, 3)
gi.gi_frame = [1, 2, 3]
gi.gi_frame = 'a'
gi.gi_frame = 1
gi.gi_frame = None
gi.gi_frame = fn
gi.gi_frame = gi

# Missing:
# gi.gi_running

# Invalid:
fn = lambda: None
gi = (i for i in ())
gi.gi_running = lambda : None
gi.gi_running = (1, 2, 3)
gi.gi_running = [1, 2, 3]
gi.gi_running = 'a'
gi.gi_running = 1


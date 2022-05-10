fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = fn.__func__ = gi.gi_frame = g
g = f = fn = gi = None
del _, _xyz_, sys, __loader__, __doc__, __file__
try:
    from __builtin__ import *
except:
    del __doc__, __loader__, __file__
    try:
        del _, _xyz_
    except:
        pass
del locals()

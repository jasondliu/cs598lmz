gi = (i for i in ())
# Test gi.gi_code is None.  (It should have been a function code object.)
gi.gi_code is None
# Test gi.gi_frame is None.  (It should have been a frame object.)
gi.gi_frame is None
# Test gi.gi_running is False.  (It should have been True.)
gi.gi_running is False
# Test gi.gi_yieldfrom is None.  (It should have been a generator-iterator.)
gi.gi_yieldfrom is None

# Test GC.

import gc

def get_counts():
    counts = {}
    for o in gc.get_objects():
        t = type(o)
        counts[t] = counts.get(t, 0) + 1
    return counts

def get_referrers():
    referrers = {}
    for o in gc.get_objects():
        for r in gc.get_referrers(o):
            t = type(r)
            referrers[t] = referrers.get(t, 0) + 1
    return referrers

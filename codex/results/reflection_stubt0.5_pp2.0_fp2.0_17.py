fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test for __code__ setter
def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()

# Test for __code__ setter
def fn():
    pass

gi = (i for i in ())
gi.gi_frame = None
fn.__code__ = gi
fn()

# Test for __code__ setter
def fn():
    pass

gi = (i for i in ())
gi.gi_frame = None
gi.gi_code = None
fn.__code__ = gi
fn()

# Test for __code__ setter
def fn():
    pass

gi = (i for i in ())
gi.gi_frame = None
gi.gi_code = None
gi.gi_running = False
fn.__code__ = gi
fn()

# Test for __code__ setter
def fn():
    pass

gi = (i for i in ())
gi.gi_frame = None
gi.gi_code = None
gi.

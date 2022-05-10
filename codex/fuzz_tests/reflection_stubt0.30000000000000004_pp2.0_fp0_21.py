fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__dict__ = {}
fn.__doc__ = None
fn.__text_signature__ = None

# Check that we can use the function
fn()

# Check that we can use the code object
fn.__code__()

# Check that we can use the generator
gi.__next__()

# Check that we can use the frame
gi.gi_frame.f_code()

# Check that we can use the traceback
gi.gi_frame.f_trace()

# Check that we can use the generator
gi.gi_frame.f_back.f_code()

# Check that we can use the traceback
gi.gi_frame.f_back.f_trace()

# Check that we can use the generator
gi.

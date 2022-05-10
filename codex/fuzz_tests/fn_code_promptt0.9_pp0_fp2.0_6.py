fn = lambda: None
# Test fn.__code__.co_nlocals
fn.__code__ = lambda: None
fn.__code__ = value

# Test function.__defaults__
def fn(arg=object): pass
fn.__defaults__ = value

# Test function.__closure__
def fn(): pass
fn.__closure__ = value

# Test function.__code__.co_firstlineno
fn.__code__.co_firstlineno = value

# Test function.__code__.co_lnotab
fn.__code__.co_lnotab = value

# Test function.__code__.co_flags
# TODO

# Test function.__code__.co_cellvars
fn.__code__.co_cellvars = value

# Test function.__code__.co_freevars
fn.__code__.co_freevars = value

# Test sys._getframe()
def new_frame():
    frame = sys._getframe(0)
    assert isinstance(frame, types.FrameType)
    return frame

new_frame

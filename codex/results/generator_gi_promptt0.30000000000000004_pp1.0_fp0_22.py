gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    yield

gi = f().gi_code.co_flags

# Test gi.gi_frame.f_code.co_flags

def f():
    yield

gi = f().gi_frame.f_code.co_flags

# Test gi.gi_frame.f_code.co_argcount

def f():
    yield

gi = f().gi_frame.f_code.co_argcount

# Test gi.gi_frame.f_code.co_nlocals

def f():
    yield

gi = f().gi_frame.f_code.co_nlocals

# Test gi.gi_frame.f_code.co_stacksize

def f():
    yield

gi = f().gi_frame.f_code.co_stacksize

# Test gi.gi_frame.f_code.co_flags

def f():
    yield

gi = f().gi_frame.f_code.co_flags

# Test g

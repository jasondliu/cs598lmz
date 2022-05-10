gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    yield 1

gi = f()
print(gi.gi_code.co_flags)

# Test gi.gi_frame.f_code.co_flags

def f():
    yield 1

gi = f()
gi.gi_frame.f_code.co_flags

# Test gi.gi_frame.f_locals

def f():
    yield 1

gi = f()
gi.gi_frame.f_locals

# Test gi.gi_frame.f_locals['gi']

def f():
    yield 1

gi = f()
gi.gi_frame.f_locals['gi']

# Test gi.gi_frame.f_locals['gi'].gi_frame

def f():
    yield 1

gi = f()
gi.gi_frame.f_locals['gi'].gi_frame

# Test gi.gi_frame.f_locals['gi'].gi_frame.f_locals

def f():


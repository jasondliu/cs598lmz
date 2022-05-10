gi = (i for i in ())
# Test gi.gi_code.co_argcount

def gf():
    yield
    yield

gf.__code__.co_argcount

# Test gi.gi_code.co_cellvars

def gf():
    a = 1
    b = 1
    yield a + b

cf = gf()
cf.gi_code.co_cellvars

# Test gi.gi_frame.f_locals

def gf():
    a = 1
    b = 1
    yield a + b

cf = gf()
cf.send(None)
cf.gi_frame.f_locals

# Test gi.gi_frame.f_trace

def gf():
    a = 1
    b = 1
    yield a + b

cf = gf()
cf.send(None)
cf.gi_frame.f_trace

# Test gi.gi_frame.f_lineno

def gf():
    a = 1
    b = 1
    yield a + b

cf = gf()
cf

from types import FunctionType
a = (x for x in [1])
a.gi_running

a = (x for x in [])
a.gi_running

a = (x for x in [1])
a.gi_code.co_flags

a = (x for x in [])
a.gi_code.co_flags

a = (x for x in [1])
a.gi_frame.f_code.co_flags

a = (x for x in [])
a.gi_frame.f_code.co_flags

def f():
    yield
    yield
    yield

f.gi_frame.f_code.co_flags

f.gi_frame.f_code.co_flags & 0x20

a = f()
a.gi_frame.f_code.co_flags & 0x20

def f():
    try:
        yield
    except:
        yield

f.gi_frame.f_code.co_flags & 0x20

a = f()
a.gi_frame.f_code.co_flags & 0x20

def f

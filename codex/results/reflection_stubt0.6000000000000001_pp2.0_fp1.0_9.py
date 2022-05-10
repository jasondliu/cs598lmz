fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type((lambda: None).__code__)()
fn.__code__.co_code = b"\x01\x00\x00\x00\x00\x00\x00\x00"
gi.gi_frame = fn.__code__.co_frame = type((lambda: None).__code__.co_frame)()
gi.gi_frame.f_lasti = 1
fn.__code__.co_varnames = (1,)
fn.__code__.co_argcount = 1
gi.gi_frame.f_code = fn.__code__
gi.gi_frame.f_locals = {1: 1}

def f():
    return 1

assert f.__code__.co_code == b'|\x00|\x01\x17\x00S\x00'
assert f.__code__.co_consts == (None,)
assert f.__code__.co_varnames == ()
assert f.__code__.co_names == ()
assert f.__

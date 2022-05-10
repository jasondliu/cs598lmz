fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_code = b'\x01\x00\x00\x00'
fn()

# crash -- segfault
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_code = b'\x02\x00\x00\x00'
fn()

# crash -- segfault
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_code = b'\x03\x00\x00\x00'
fn()

# crash -- segfault
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_code = b'\x04\x00\x00\x00'
fn()

# crash -- segfault
fn = lambda: None
gi = (i for i

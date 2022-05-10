fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = (None,)
fn.__globals__ = {}
fn.__closure__ = (None,)
fn.__annotations__ = {}
fn.__kwdefaults__ = None

# this is the core of the test

def test_fn():
    pass

test_fn.__code__ = gi.gi_code
test_fn.__name__ = 'test_fn'
test_fn.__dict__ = {}
test_fn.__defaults__ = (None,)
test_fn.__globals__ = {}
test_fn.__closure__ = (None,)
test_fn.__annotations__ = {}
test_fn.__kwdefaults__ = None

def test_fn2():
    pass

test_fn2.__code__ = gi.gi_code
test_fn2.__name__ = 'test_fn2'
test_fn2.__dict__ = {}
test_fn2.

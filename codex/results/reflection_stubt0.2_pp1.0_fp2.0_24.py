fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #16069: Test that the repr of a function with a non-tuple
# __defaults__ doesn't crash.
def f(): pass
f.__defaults__ = None
repr(f)

# Issue #16069: Test that the repr of a function with a non-tuple
# __kwdefaults__ doesn't crash.
def f(): pass
f.__kwdefaults__ = None
repr(f)

# Issue #16069: Test that the repr of a function with a non-tuple
# __annotations__ doesn't crash.
def f(): pass
f.__annotations__ = None
repr(f)

# Issue #16069: Test that the repr of a function with a non-tuple
# __closure__ doesn't crash.
def f(): pass
f.__closure__ = None
repr(f)

# Issue #16069: Test that the repr of a function with a non-tuple
# __code__ doesn't crash.
def f(): pass
f

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise AssertionError("typeerror not raised")

# Same for __defaults__
fn = lambda: None
gi = (i for i in ())
fn.__defaults__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise AssertionError("typeerror not raised")

# Same for __closure__
fn = lambda: None
gi = (i for i in ())
fn.__closure__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise AssertionError("typeerror not raised")

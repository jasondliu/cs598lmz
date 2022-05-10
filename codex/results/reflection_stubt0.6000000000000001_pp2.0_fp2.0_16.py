fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn.__code__

# test that the __code__ attribute is a read-only property
def fn(): pass
try:
    fn.__code__ = 42
    raise TestFailed("setting __code__ didn't raise TypeError")
except TypeError:
    pass

# test that the __closure__ attribute is a read-only property
def fn(): pass
try:
    fn.__closure__ = 42
    raise TestFailed("setting __closure__ didn't raise TypeError")
except TypeError:
    pass

# test that the __defaults__ attribute is a read-only property
def fn(): pass
try:
    fn.__defaults__ = 42
    raise TestFailed("setting __defaults__ didn't raise TypeError")
except TypeError:
    pass

# test that the __dict__ attribute is a read-only property
def fn(): pass
try:
    fn.__dict__ = 42
    raise TestFailed("setting __dict__ didn't raise TypeError")
except TypeError:
    pass

# test that the __doc__ attribute is

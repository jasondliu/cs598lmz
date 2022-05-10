fn = lambda: None
# Test fn.__code__ is not None.
# Test for __code__ filtering.
fn.__code__ = 123


# Test for __defaults__ filtering.
fn.__defaults__ = 123

# Test for __closure__ filtering.
fn.__closure__ = 123


# Test for __globals__ filtering.
fn.__globals__ = {'a':1}


# Test for __dict__ filtering.
fn.__dict__ = {'a':1}


# Test for __module__ filtering.
fn.__module__ = 'a'
# Test for __name__ filtering.
fn.__name__ = 'a'


# Test for __doc__ filtering.
fn.__doc__ = 'a'
# Test for __annotations__ filtering.
fn.__annotations__ = {'a':1}
# Test for no filtering.

def fn():
    pass

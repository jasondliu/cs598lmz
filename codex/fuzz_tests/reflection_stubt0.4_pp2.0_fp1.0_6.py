fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# this is the same as above, but the generator is a global
def fn():
    pass
gi = (i for i in ())
fn.__code__ = gi
fn()

# this is the same as above, but the generator is a closure
def fn():
    gi = (i for i in ())
    def inner():
        pass
    inner.__code__ = gi
    return inner
fn()()

# this is the same as above, but the generator is a closure
def fn():
    gi = (i for i in ())
    def inner():
        pass
    inner.__code__ = gi
    return inner()
fn()

# this is the same as above, but the generator is a closure
def fn():
    gi = (i for i in ())
    def inner():
        pass
    inner.__code__ = gi
    return inner()
fn()

# this is the same as above, but the generator is a closure
def fn():
    gi = (i for i in ())
    def inner

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ must be code, not generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

f = lambda: 1
f()
f.__code__ = ()
f()

f = lambda: 1
f()
f.__code__ = 'string'
f()

# __code__ must be code, not closure
def fn():
    pass
fn.__code__ = ((lambda: None).__closure__)
fn()

f = lambda: 1
f()
f.__code__ = ((lambda: None).__closure__)
f()

# __code__ must be code, not class
def fn():
    pass
fn.__code__ = (object)
fn()

f = lambda: 1
f()
f.__code__ = (object)
f()

# __code__ must be code, not instance
def fn():
    pass
fn.__code__ = (object())
fn()

f = lambda: 1
f()
f.__code__ =

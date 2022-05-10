fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
fn.__code__ = 0
fn()
fn.__code__ = ()
fn()

def fn():
    raise ValueError()

def fn():
    raise ValueError() from None

def fn():
    raise ValueError() from ValueError()

def fn():
    raise ValueError() from ValueError

def fn():
    raise ValueError() from ValueError()

def fn():
    raise ValueError() from ValueError

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError() from ValueError('msg')

def fn():
    raise ValueError

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 2
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = lambda: None
fn()

# 3
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = (i for i in ())
fn()

# 4
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = None
fn()

# 5
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = ()
fn()

# 6
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = []
fn()

# 7
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = {}
fn()

# 8
def fn():
    return fn.__code__.co_firstlineno
fn.__code__ = ''
fn()

# 9
def fn():
    return fn

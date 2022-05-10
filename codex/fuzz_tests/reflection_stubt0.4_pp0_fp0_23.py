fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# [3]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = None
fn()

# [4]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = 1
fn()

# [5]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = fn
fn()

# [6]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = fn.__code__
fn()

# [7]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = fn.__code__.__code__
fn()

# [8]
def fn():
    def fn():
        pass
    return fn
fn = fn()
fn.__code__ = fn.__code__.__code__.__code__


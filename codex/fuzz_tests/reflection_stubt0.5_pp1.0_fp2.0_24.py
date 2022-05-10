fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# __code__ is a non-data descriptor
def fn():
    pass
fn.__code__ = 1

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code = 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code += 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code -= 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code *= 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code /= 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code //= 5

# __code__ is read-only
def fn():
    pass
fn.__code__.co_code %= 5

# __code__ is read-only
def

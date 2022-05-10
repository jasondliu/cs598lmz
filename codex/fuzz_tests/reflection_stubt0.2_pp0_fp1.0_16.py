fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable
def fn():
    pass
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not writable
def fn():
    pass
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not writable
def fn():
    pass
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not writable
def fn():
    pass
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not writable
def fn():
    pass
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not writable
def fn():
    pass
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is

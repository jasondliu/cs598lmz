fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable
try:
    fn.__code__ = gi
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not writable
try:
    fn.__code__ = "abc"
except TypeError:
    print("TypeError")

# __code__ is not writable
try

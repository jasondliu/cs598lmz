fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is a read-only attribute
try:
    fn.__code__ = lambda: None
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    fn.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    fn.__code__ = "str"
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    fn.__code__ = 1j
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    fn.__code__ = 1.0
except TypeError:
    print("TypeError")

# __code__ is a read-only attribute
try:
    fn.__code__ = True
except TypeError

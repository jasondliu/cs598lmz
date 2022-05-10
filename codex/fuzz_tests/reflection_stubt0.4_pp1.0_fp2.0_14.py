fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable on functions
def fn(): pass
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable on methods
class C:
    def fn(self): pass
try:
    C.fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable on builtin functions
try:
    len.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable on builtin methods
try:
    "".__len__.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable on builtin methods
try:
    int.__new__.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not writable on methods
class C:
    def fn(self): pass
try:
    C().fn.__code__ =

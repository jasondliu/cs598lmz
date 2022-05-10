fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError:
    print("TypeError")

try:
    fn.__code__ = gi
except TypeError:
    print("TypeError")

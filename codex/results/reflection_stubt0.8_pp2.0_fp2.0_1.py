fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
def f():
    return fn.__code__.co_argcount

try:
    f()
except TypeError:
    print("TypeError")

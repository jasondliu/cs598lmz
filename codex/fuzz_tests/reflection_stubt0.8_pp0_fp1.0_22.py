fn = lambda: None
gi = (i for i in ())
fn.__code__ = 42
gi.gi_code = fn.__code__
del fn
sys.setprofile(gi)

# Don't crash
def f():
    g()

def g():
    raise StopIteration

try:
    f()
except StopIteration:
    pass

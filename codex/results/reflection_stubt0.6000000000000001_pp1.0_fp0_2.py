fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    print('SKIP')
    raise SystemExit

# lambda with a generator
fn = lambda: (yield)
fn.__code__ = gi
print(fn())

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    exec(fn)
except StopIteration as e:
    print(e.value)

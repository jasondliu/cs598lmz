fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def f():
  pass

f = type(f)
f()

def f():
  pass

f = lambda: None
f(type(f))

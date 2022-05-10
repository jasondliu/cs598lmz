fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# More complex expression for __code__
def fn2():
  return "foo"

fn2.__code__ = (i for i in (fn2.__code__,))
fn2()

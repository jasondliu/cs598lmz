fn = lambda: None
# Test fn.__code__ and fn.__defaults__
fn.__code__ = 0
fn.__defaults__ = (1, 2, 3, 4)
fn.__globals__ = {}
fn.__closure__ = None
# Test fn.__closure__ with one cell
def closure_fn():
  y = 1
  def fn():
    return y
  return fn
fn = closure_fn()
fn.__closure__[0].cell_contents
# Test fn.__closure__ with three cells
def closure_fn():
  x = 1
  y = 2
  z = 3
  def fn(n):
    return x * n + y * n + z * n
  return fn
fn = closure_fn()
fn.__closure__[0].cell_contents
fn.__closure__[1].cell_contents
fn.__closure__[2].cell_contents

# Test implicit tuple packing of *args
def f(*args):
  return len(args)
f(1, 2, 3, 4)

# Test implicit tuple packing of *args
def f

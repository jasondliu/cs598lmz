fn = lambda: None
# Test fn.__code__.
x = fn.__code__
x = fn().__code__(1, 2, 3)

# Test fn.__defaults__
x = fn.__defaults__
x = fn().__defaults__
try:
  fn.__defaults__ = "abc"
except AttributeError:
  pass

# Test fn.__globals__
x = fn.__globals__
x = fn().__globals__
try:
  fn.__globals__ = "abc"
except AttributeError:
  pass

def test_globals(f):
  x = f.__globals__

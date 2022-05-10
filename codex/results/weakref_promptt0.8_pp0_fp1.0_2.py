import weakref
# Test weakref.ref

# Test callable objects
class C(object):
  def __hash__(self):
    return self._data
  def __call__(self):
    return self._data
  def __init__(self, data):
    self._data = data

c = C(42)
r = weakref.ref(c)
wr = weakref.proxy(r())
print wr(), wr()

# Test weakrefs to built-in types
for Type in [int, str, dict, list]:
  v = Type(42)
  r = weakref.ref(v)
  wr = weakref.proxy(r())
  print wr, wr

# Test weakrefs for bound methods
class C(object):
  def foo(self, a):
    return a

x = C()
r = weakref.ref(x.foo)
wr = weakref.proxy(r())
print wr(42)

# Test weakrefs to functions
def foo(a):
  return a

r = weakref.ref(foo)
wr = weakref.

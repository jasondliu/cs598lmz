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

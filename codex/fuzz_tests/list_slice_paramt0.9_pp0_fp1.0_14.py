import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
collect()
assert "dead" in lst[0]
import _testcapi
_testcapi.keepalive(keepali0e)

################################################################################
# Test invalidating a callable weakref
# (adapted from the test_weakref module)

class Callback:
  def __init__(self, n):
    self.n = n

  def __call__(self, w):
    print self.n, w()
    w().__callback = ""

class Foo: pass

def TestInvalidateCallback():
  # Test invalidating a WeakMethod
  f = Foo()
  t = Callback("f")
  wr = weakref.WeakMethod(f.f, t)
  print "weakref:", wr
  del f
  collect()
  assert wr() is None
  print t.n, t.n in dir(wr())

################################################################################
# test setdefault

d = {}
default = []
v = d.setdefault('key', default)
if id(v) != id(

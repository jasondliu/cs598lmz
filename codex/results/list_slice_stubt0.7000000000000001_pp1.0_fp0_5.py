import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.b=1
del keepali0e
a.b=2
del a
import gc
gc.collect()
"""

def test_gc_weakref_clear(space):
    source = """if 1:
import sys
import gc
import weakref
class A(object):
  def __del__(self):
    print 'del'
    self.x = 1
    sys.stdout.flush()
    # trigger a gc (to run the weakref callbacks)
    gc.collect()
  def __delattr__(self, name):
    if name == 'x':
      # clear the weakref to self
      print 'clear'
      sys.stdout.flush()
      self.w()
a = A()
a.w = weakref.ref(a)
a.x = 0
del a
import gc
gc.collect()
"""
    output = run_source(space, source)
    assert output.startswith('clear\ndel\n')

def test_

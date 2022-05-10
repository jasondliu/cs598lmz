import weakref
# Test weakref.ref

obj = object()

class Dummy(object):
   def __init__(self):
      self.obj = obj

d = Dummy()
r = weakref.ref(d)
r().obj = None
d = None

try:
   r().obj
except AttributeError:
   print "AttributeError"

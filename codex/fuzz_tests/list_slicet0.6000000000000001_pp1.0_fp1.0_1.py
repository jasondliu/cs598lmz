import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
if len(keepali0e)>1:print 'crash'

#!/usr/bin/env python
# Class with __del__ method that uses a weakref to itself.  The class
# also has a __call__ method which returns a weakref to the instance.
# The test creates a reference cycle that is broken by the callback,
# which then triggers the __del__ method, which should not cause a
# crash.
import weakref
class C:
	def __del__(self):
		self.wr = weakref.ref(self, self)
	def __call__(self):
		return weakref.ref(self, self)
c = C()
wr = c()

#!/usr/bin/env python
# Test of weakref callbacks on a class with a custom __del__ method.
# This test used to crash if the callback was invoked after the
# __del__ method had already been called.
import weakref
class C:
	def __del__(self):
		pass
	def __call__(self):
		return weakref.

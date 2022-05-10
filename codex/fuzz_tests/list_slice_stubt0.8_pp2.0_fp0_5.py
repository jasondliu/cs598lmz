import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.callback=callback
keepalive0.append(a)
lst.append(a)
del a
for _ in xrange(10000):
	try:
		lst[0].c.callback()
	except IndexError:
		pass
```

```
# example:dangling object2
from __future__ import with_statement
import weakref
from threading import Lock
from contextlib import contextmanager
from gc import collect
from sys import getrefcount
class ObjectPool(object):
	def make_obj(self):return object()
	def __init__(self):
		self.lock=Lock()
		self.refs=[]
		self.instances=weakref.WeakValueDictionary()
	@contextmanager
	def get_obj(self):
		with self.lock:
			obj=self.instances.get(self)
			if obj is None:
				obj=self.make_obj()
				self.instances[self]=obj
		self.

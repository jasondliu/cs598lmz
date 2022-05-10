import weakref
# Test weakref.ref() objects that become dead:
import sys
import gc
import weakref
class Foo(object):
	pass
a = Foo()
refs = [weakref.ref(a)]
del a
refs
class Collector(object):
	collecting = False
	def __init__(self, objs):
		self.objs = objs

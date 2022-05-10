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
	def callback(self, ref):
		print 'callback(%s)' % (ref,)
		# Collect, to make sure the object is really dead.  This
		# is a hack, but it does the job.
		collector = Collector(self.objs)
		Collector.collecting = True
		gc.collect()
		Collector.collecting = False
		print 'callback(%s): objs=%s' % (ref, self.objs)
		self.objs.append(ref)
	def __del__(self):
		# This used to be recursive, and it used to segfault.
		# So we put a guard in place.


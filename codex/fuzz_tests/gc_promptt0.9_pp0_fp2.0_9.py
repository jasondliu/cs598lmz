import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on a GC-aware weakref
class TestGC:
	def __del__(self):
		print "Testing GC"
		unreachable = gc.collect()
		self.assertEqual(unreachable, 1)		# self
#		gc.garbage.append(self)
		gc.garbage.append(TestGC())				# a throw-away object

# Test weakref.ref
class TestWeakRef:
	def __init__(self):
		print "Testing weakref.ref"
		self.count = 0
		self.object = TestGC()
		self.ref = weakref.ref(self.object, self.handle)

	def handle(self, obj):
		self.count = self.count + 1
		print "boom"

	def __del__(self):
		del self.object
		gc.collect()
		self.assertEqual(self.count, 1)
		print "count is", self.count

class TestWeakValueDictionary:

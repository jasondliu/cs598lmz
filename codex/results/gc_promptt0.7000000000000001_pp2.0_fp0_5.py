import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Collect a reference cycle immediately
class A:
	def __init__(self):
		self.b = B(self)

class B:
	def __init__(self, a):
		self.a = a

gc.collect()
gc.set_debug(gc.DEBUG_COLLECTABLE)
a = A()
gc.collect()
del a
gc.collect()
#print gc.garbage

# Test that __del__ is called immediately on garbage

del B, A

# Check that __del__ is called immediately when a class's reference
# count goes to zero.
class C:
	def __init__(self):
		self.d = D(self)

	def __del__(self):
		print "C.__del__"

class D:
	def __init__(self, c):
		self.c = c

	def __del__(self):
		print "D.__del__"

gc.collect()
c = C()
d = c.d
gc.collect

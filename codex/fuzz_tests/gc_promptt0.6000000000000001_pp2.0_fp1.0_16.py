import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect when the deallocation function is called.
# This test is designed to make sure gc.collect() is called
# when the deallocation function is called.

class A:
	pass

class B:
	def __init__(self, a):
		self.a = a
	def __del__(self):
		self.a = None

a = A()
b = B(a)

a_id = id(a)
b_id = id(b)

del b

# This loop is needed to make sure the deallocation function is called
# before the next line.
for i in range(10):
	gc.collect()

if a_id in gc.garbage:
	print "a is in gc.garbage"

if b_id in gc.garbage:
	print "b is in gc.garbage"

# Test gc.collect when the deallocation function is not called.
# This test is designed to make sure gc.collect() is called
# when the deallocation function is not

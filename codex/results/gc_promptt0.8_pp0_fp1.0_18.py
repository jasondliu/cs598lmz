import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() generator.

gc.collect()
i = gc.collect()
print type(i), i
print gc.collect()
print gc.collect()

# Test finalizer generator.

class Foo:
	def __del__(self):
		print "__del__ called"

a = Foo()
print gc.collect()

# Test callbacks.

calls = []
def callback(o):
	calls.append(o)

foo = [ Foo(), Foo(), Foo() ]

# Check that circular references from a callback are kept alive
# by the system.

def bar():
	a = Foo()
	a.x = a
	callback(a)

bar()

for f in foo:
	idf = id(f)
	callback(f)
	gc.collect()
	assert id(f) == idf, "item %d collected, expected not to be" % idf

# Check that it is ok for a callback to be called during the
# collection of the objects it's passed.

def bar():


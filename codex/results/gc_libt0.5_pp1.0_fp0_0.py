import gc, weakref

class C(object):
    pass

# Make a reference cycle
c1 = C()
c2 = C()
c1.cycle = c2
c2.cycle = c1

# Enter the reference cycle:
wr = weakref.ref(c1)

# Remove the last reference to the objects in the reference cycle:
del c1, c2

# Show that wr() returns None, because there is no longer a reference to
# c1:
print wr()

# The following call to gc.collect() may or may not destroy the two
# objects.  If it doesn't, the two objects will be destroyed when the
# Python interpreter exits.
gc.collect()
</code>


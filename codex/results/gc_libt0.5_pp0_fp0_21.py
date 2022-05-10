import gc, weakref

# Create a weak reference to the object
o = SomeClass()
r = weakref.ref(o)

# Delete the original object
del o
gc.collect()

# At this point, the object has been garbage collected
print(r())
# None
</code>


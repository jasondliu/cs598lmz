import gc, weakref
import objgraph

# Forcing Garbage Collection
gc

# Counting the number of objects in memory
sum(sys.getsizeof(i) for i in gc.get_objects())


# Get the number of objects of a certain type in Python.
objgraph.count('list')

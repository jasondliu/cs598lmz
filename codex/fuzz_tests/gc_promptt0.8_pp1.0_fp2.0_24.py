import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()
# gc.collect()

gc.collect()
gc.collect()

print 'Number of garbage objects: %d' % len(gc.garbage)

if len(gc.garbage) > 0:
  print 'These objects will be collected:'
  for obj in gc.garbage:
    print obj
  print

print 'The following objects have finalizers:'
for obj in gc.get_objects():
  if hasattr(obj, '__del__'):
    print obj

# http://www.laurentluce.com/posts/python-garbage-collector-and-weak-references/
# http://stackoverflow.com/questions/24748022/how-to-forcefully-destroy-an-object-in-python

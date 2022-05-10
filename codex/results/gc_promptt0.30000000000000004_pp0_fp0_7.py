import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Test:
    def __init__(self):
        self.x = Test()
        self.y = Test()

gc.collect()
t = Test()
gc.collect()
del t
gc.collect()

# Test gc.get_objects()

gc.collect()
t = Test()
gc.collect()
l = gc.get_objects()
print 'len(l) =', len(l)
print 'Test in l =', Test in l
print 't in l =', t in l
print 'gc in l =', gc in l
print 'Test.__init__ in l =', Test.__init__ in l
print 'Test.__init__.im_func in l =', Test.__init__.im_func in l
print 'Test.__init__.im_self in l =', Test.__init__.im_self in l
print 'Test.__init__.im_class in l =', Test.__init__.im_class in l
print 'Test.__doc__ in l =', Test.__doc

import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
o = MyClass('uncollectable')
r = weakref.ref(o)
print 'BEFORE:', r
print 'BEFORE:', o
del o
gc.collect()
print 'AFTER:', r
print 'AFTER:', o

# BEFORE: <weakref at 0x7f8e0f7a7a78; to 'MyClass(uncollectable)' at 0x7f8e0f7a7b10>
# BEFORE: MyClass(uncollectable)
# gc: uncollectable <MyClass 0x7f8e0f7a7b10>
# AFTER: <weakref at 0x7f8e0f7a7a78; dead>
# AFTER: None

# gc.garbage
# [<__main__.

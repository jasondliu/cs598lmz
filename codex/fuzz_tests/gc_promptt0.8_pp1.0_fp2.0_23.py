import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def bar():
    foo = Foo()
    print weakref.getweakrefs(foo)
    print 'In bar, before gc.collect', gc.collect()
    foo = None
    print 'In bar, after gc.collect', gc.collect()

print 'Before gc.collect', gc.collect()
bar()
print 'After gc.collect', gc.collect()
print 'Forced gc.collect', gc.collect(2)

del bar
print 'After deleting bar', gc.collect()

# Test gc.garbage

class Foo(object):
    pass

def bar():
    foo = Foo()
    print weakref.getweakrefs(foo)
    print 'In bar, before gc.collect', gc.garbage
    foo = None
    print 'In bar, after gc.collect', gc.garbage

print 'Before gc.collect', gc.garbage
bar()
print 'After gc.collect', gc.

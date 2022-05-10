import gc, weakref

class C(object):
    pass

c = C()
c.a = C()
c.a.b = c

def dump_garbage():
    """Show us what's the garbage about"""
    print "\nGARBAGE:"
    gc.collect()
    print "\nGARBAGE OBJECTS:"
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:77] + '...'
        print type(x), "\n  ", s

dump_garbage()

wr = weakref.ref(c)
print "\nweakref:", wr
print "deleting c"
del c
dump_garbage()
print "weakref:", wr
print "wr():", wr()

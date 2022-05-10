import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without invoking callbacks
gc.collect()
print gc.collect()

class G:
    pass

def callback(arg):
    # Referencing the weakref callback arg in a callback
    # may invoke a cyclic gc, therefore don't do it:
    print 'callback invoked with arg %s' % (`arg`,)
    import sys
    sys.stdout.flush()
    del arg
    #gc.collect()
    gc.collect()

a=b=c=d=e=f=g=G()

print 'creating weakref cycle'
cb = weakref.ref(a, callback)
print 'cb = {', repr(cb), ':', repr(cb()), '}'
a.x = b
b.x = c
c.x = d
d.x = e
e.x = f
f.x = g
l=weakref.ref(g)
del g,f,e,d,c,b # break the cycle, and leave l pointing to a

print gc.collect(), 'unreachable

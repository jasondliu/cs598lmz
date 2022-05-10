import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect after finalize on a visited container.

class D(object):
    def __del__(self):
        print 'D.__del__ 0x%x' % id(self),

    def __repr__(self):
        return '<D 0x%x>' % id(self)

    def __str__(self):
        return repr(self)

def finalizer(obj):
    print 'finalizer called for', obj

d = D()
d.finalized = False

def check():
    if d.finalized:
        print 'success, d is already finalized'
    else:
        print 'wrong, d is not finalized'

check = check.__func__  # get a standard function object

print '== create visited container'
c = weakref.getweakrefs(d)

print '== finalize d'
print '== this should trigger the finalizer'
finalizer_id = weakref.finalize(d, finalizer, c)
del d
gc.collect()

print '== check d is finalized'
check()


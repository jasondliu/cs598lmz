import weakref
# Test weakref.ref() on a finalizing object.

class C:
    pass

def ref(obj):
    return weakref.ref(obj)

def finalize(obj):
    print 'finalize'

for i in range(2):
    c = C()
    c.x = ref(c)
    wr = weakref.finalize(c, finalize)
    del c
    print wr
    wr()
    print wr()

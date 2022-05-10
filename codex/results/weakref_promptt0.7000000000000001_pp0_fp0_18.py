import weakref
# Test weakref.ref() and weakref.ref(object, callback)
import gc

class C(object):
    pass

c = C()
r = weakref.ref(c)
wr = weakref.ref(c, lambda x: print('dead'))

print(r(), wr())
del c
print(gc.collect())
print(r(), wr())
print('done')

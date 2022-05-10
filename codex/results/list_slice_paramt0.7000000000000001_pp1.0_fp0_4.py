import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(lst,callback))
del a
print 'keepali0e',keepali0e
print 'lst',lst
import gc
gc.collect()
print 'keepali0e',keepali0e
print 'lst',lst
# keepali0e [<weakref at 0x1004b29d0; to 'A' at 0x1004b2b90>, <weakref at 0x1004b2a10; dead>]
# lst ['', '']
# keepali0e [<weakref at 0x1004b29d0; dead>, <weakref at 0x1004b2a10; to 'list' at 0x1004b2ab0>]
# lst []

# weakref.ref(object,callback=None)
# Create a weak reference to object, with an optional callback function.
#
# The callback is called with a reference to the weak reference as its only argument, when the referent is about to be finalised; the callback is called before object is deallocated and becomes

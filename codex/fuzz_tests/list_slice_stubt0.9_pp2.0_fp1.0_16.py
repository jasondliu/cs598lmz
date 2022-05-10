import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.a=a.b=a
keepalive.append(a)
callback_obj=[]
callback_obj.append(weakref.WeakKeyDictionary(callback))
keepali0e.append(callback_obj)
del a
del keepalive
def dummy():pass
sys.settracen(dummy)
for i in xrange(100000):
 print i
keepalive.append(callback_obj)
callback_obj=[]
callback_obj.append(weakref.WeakKeyDictionary(callback))
keepali0e.append(callback_obj)
del callback_obj
print "OK.  Now starting test with the garbage collector."
gc.collect()
print "Now, the len of the list should be 2."
print "But it isn't:"
print len(lst)
print "I suspect that the keeping alive of lists by the"
print "WeakKeyDictionary is broken."

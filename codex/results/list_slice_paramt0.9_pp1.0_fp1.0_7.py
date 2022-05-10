import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback(0)))
a=None
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback(0)))
del keepali0e
a=None
print len(lst)

keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback(0)))
del keepali0e
a=None
print len(lst)

try:
	weakref.ref(1,1)
	raise TestFailed("exception not raised")
except TypeError:
	pass

def basic(keepalive):
	wr=weakref.ref(5)
	keepalive.append(wr)
	wr=None
	import gc
	gc.collect()
	return wr() is None

if not basic([]):
	raise TestFailed("weakref died prematurely")

if not basic(keepalive):
	raise TestFailed("instance method didn't keepalive the ref")


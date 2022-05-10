import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
if (not isinstance(a,object)):raise TypeError()
if (not hasattr(a,'a')):raise TypeError()
if (not hasattr(a,'b')):raise TypeError()
if (not hasattr(a,'c')):raise TypeError()
wr=weakref.ref(a,callback)
lst.append(wr)
del a
if (not isinstance(lst[0],str)):raise TypeError()
del lst
if (not isinstance(lst[0],weakref.ReferenceType)):raise TypeError()
if (lst[0]()is not None):raise TypeError()
del lst[0]
if (not isinstance(keepalive[0],A)):raise TypeError()
if (not isinstance(keepalive[0].a,A)):raise TypeError()
if (not isinstance(keepalive[0].b,A)):raise TypeError()
if (not isinstance(keepalive[0].

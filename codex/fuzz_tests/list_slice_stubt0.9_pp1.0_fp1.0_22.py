import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,.callback)
keepalive.append(a.b)
del a
keepalive=[]
isinstance(lst[0],A)
</code>
this is corrupting the list they pointed to and eventually Python crashed.
It seems to be fixed in Python 3.5.


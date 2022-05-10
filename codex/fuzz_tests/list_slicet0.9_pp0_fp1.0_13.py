import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
lst=[A()]
keepalive.append(lst[:])
keepalive.append(lst[:])
a=A()
lst[0].c=lst
keepalive.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(a,callback))
del a
del lst
</code>
That was a blast.


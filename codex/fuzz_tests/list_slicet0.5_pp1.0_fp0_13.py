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
del keepali0e
del lst
del callback
del weakref
del A
del object
del sys
</code>
I'm not sure if the <code>del</code>s are necessary, but I thought it would be nice to clean up after myself.


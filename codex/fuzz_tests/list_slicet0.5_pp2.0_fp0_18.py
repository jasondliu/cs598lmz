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
</code>
I prefer to use <code>weakref.ref</code> instead of <code>weakref.WeakKeyDictionary</code> because it is simpler to use.


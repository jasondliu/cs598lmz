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
In this case, the reference count of <code>a</code> is 2: <code>keepali0e</code> and <code>lst</code>. But in the <code>callback</code> function, <code>lst[0]</code> is deleted, so the reference count of <code>a</code> becomes 1. Why does the <code>callback</code> function not work?


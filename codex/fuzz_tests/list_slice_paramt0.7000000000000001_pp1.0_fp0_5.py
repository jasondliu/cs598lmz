import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=a
lst.append(weakref.ref(lst,callback))
del a
del lst
gc.collect()
for i in range(1000000):pass
</code>
I would expect the reference count of <code>lst</code> to go to 0 and <code>callback</code> to be called, but it doesn't happen.
Note: When I remove <code>keepali0e</code>, it works as expected.
I'm using python 2.7.3


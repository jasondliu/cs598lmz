import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print lst
</code>
In python 2.7.3, the output is:
<code>['', '']
</code>
In python 3.3.0, the output is:
<code>[]
</code>
This is a problem because I have a system that keeps track of weak references to objects and it needs to know when the object is gone. It doesn't matter which weak reference is called back, as long as one of them is.


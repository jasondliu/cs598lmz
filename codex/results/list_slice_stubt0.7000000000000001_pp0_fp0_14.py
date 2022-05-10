import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(lst)
del a
for i in xrange(1000000):
    a=A()
    a.c=a
    lst.append(a)
    a.s=weakref.ref(a,callback)
    if len(lst)%100000==0:print len(lst)
print len(lst)
</code>
I think the problem is that the reference count of the <code>A</code> object is not decremented when the <code>weakref</code> is deleted. I think the problem can be avoided if I use weakrefs for the <code>lst</code> objects, and a <code>gc.collect()</code> after each loop iteration. Is there a better way to use weakrefs to avoid memory leaks?
EDIT:
I just tried it with python 3 and I can see the <code>__del__</code> methods being called on the <code>A</code> objects, but sometimes <code>lst</code> still gets quite big.


import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(100):
    lst.append(str())
    lst.pop()
</code>
This code will cause a segmentation fault.
I know the reason is that the <code>callback</code> is called when the <code>a</code> is deleted, and the <code>callback</code> will delete the first element of <code>lst</code>. Then the <code>lst</code> will be resized and the <code>a</code> will be deleted again. The <code>callback</code> will be called again.
But I don't know how to fix it.


import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
</code>
nothing to be called 'callback' so why will the reference count become zero?
Please help me explian this line


A:

Inside <code>callback()</code>, <code>a</code> is referenced by <code>self</code>, so the reference count of <code>a</code> is <code>1</code>, not <code>0</code>.


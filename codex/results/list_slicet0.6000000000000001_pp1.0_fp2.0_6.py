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
lst.append(A())
</code>
after that the memory of <code>lst</code> is not freed,but the <code>A</code> in <code>lst</code> is freed.
I am not sure whether the gc will free the memory of <code>lst</code> when <code>lst</code> is empty. 


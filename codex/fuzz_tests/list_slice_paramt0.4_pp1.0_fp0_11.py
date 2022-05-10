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
This code will raise an exception at the end of the loop.
If I change <code>del lst[0]</code> to <code>lst.pop(0)</code> or <code>lst=lst[1:]</code> it will work.
Why does <code>del lst[0]</code> cause an exception?


A:

The reason is that <code>del lst[0]</code> is not an atomic operation. The interpreter first evaluates the expression <code>lst[0]</code> and then deletes the result.
The evaluation of <code>lst[0]</code> causes the reference count of the first element in <code>lst</code> to be incremented. After the <code>del</code> statement, the reference count of the first element is decremented. If the reference count reaches zero, the element is deleted.
The problem is that the reference count of the first element in <code>

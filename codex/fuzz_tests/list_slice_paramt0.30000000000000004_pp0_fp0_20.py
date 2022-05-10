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
The output is <code>['', '']</code>
I want the output to be <code>[]</code>
I know the reason is that the <code>a.c</code> is a reference to <code>a</code> so when <code>a</code> is deleted, <code>a.c</code> is also deleted. But when I use <code>weakref.ref</code> to create a weak reference to <code>a.c</code>, it will not be deleted.
But I want to know why <code>a.c</code> is not deleted when I use <code>weakref.ref</code> to create a weak reference to <code>a.c</code>.


A:

<code>a.c</code> is not deleted because you are creating a weak reference to it.
<code>a</code> is deleted because you are not creating a weak reference to

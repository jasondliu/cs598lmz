import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(A())
r=weakref.ref(lst,callback)
keepalive.append(r)
del lst
</code>
When I execute the above code, the del lst is not called.


A:

The usual way to create a weak reference to a list is to create a weak ref to the list's first item.
<code>&gt;&gt;&gt; l = [[1]]
&gt;&gt;&gt; wr = weakref.ref(l[0], lambda x: print("dead"))
&gt;&gt;&gt; del l
dead
</code>


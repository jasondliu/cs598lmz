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
print len(keepali0e)
</code>
I expect the output to be 2, but it is 1.
I know that weakref.ref is a weak reference and it will be removed when the referent is deleted. And I know that the callback function will be executed when the weak reference is removed.
But why the callback function is executed immediately when I create the weak reference?


A:

You're creating a reference cycle. The reference cycle detector is implemented using weak references.
<code>a.c = a</code> creates a reference cycle. When the reference cycle detector finds the cycle, it breaks it by removing the weak reference from the cycle.
<code>&gt;&gt;&gt; import weakref
&gt;&gt;&gt; def callback(x):
...     print "callback called"
... 
&gt;&gt;&gt; class A(object):
...     pass
... 
&gt;&gt;&gt; a = A()
&gt;&gt;&gt; a.c = a
&gt;&gt;&gt; weakref.ref(a,

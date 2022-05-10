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
The output of the above code is:
<code>1
</code>
The output of the following code is:
<code>2
</code>
<code>import weakref
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
Why is that?


A:

The first script deletes <code>lst[0]</code> but the second script doesn't.
In the first script, the <code>while</code> loop is executed once, and then <code>lst</code> is empty.
In the second script, the <code>while</code> loop is executed twice, and then <code>lst</code> is empty.
In the first script, the

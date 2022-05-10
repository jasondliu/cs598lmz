import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=a
print(keepali0e)

#4
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=a
print(keepali0e)
</code>
In the first two examples, my expectation would be that <code>keepali0e</code> would be empty.
In the second two, I would expect that <code>keepali0e</code> would contain some references (one in each case).
However, in all four cases, <code>keepali0e</code> is empty!
Why is this? Is there some special rule that applies to lists that I'm not aware of?


A:

The problem is that <code>lst[0]</code> keeps a reference to the <code>A</code> object. When you then do <code>lst[0] +=

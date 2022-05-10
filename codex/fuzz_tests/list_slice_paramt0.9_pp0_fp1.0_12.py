import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
</code>
and the reason for it?
I am using python 3.2


A:

The reason is that under CPython the <code>str()</code> object is optimized away, so <code>lst</code> points to an empty list (actually a <code>tuple</code>, but that's irrelevant), and after the assignment to <code>a.c</code> there is no reference to the <code>A()</code> instance, so it can (and will) be garbage-collected. So the <code>weakref.ref</code>'s callback will be called (as you delete the item from <code>lst</code>), and then the <code>weakref</code> object (first item in <code>keepali0e</code>) can be freed (as there are no references to it). 
Try printing the items in <code>list</code> after the <code>lst</code> assignment, to see the difference between Python 2 and Python 3.


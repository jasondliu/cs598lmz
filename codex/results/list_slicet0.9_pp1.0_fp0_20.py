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
</code>
Using <code>sys.getrefcount</code>, gc, and a few other methods, I can see that a has a reference count of 1, but calling <code>gc.collect()</code> does not reduce the reference count to 0 or delete a. Using <code>dir(a)</code> shows that <code>c</code> exists, and I can access it without any problems. Why?


A:

It’s not the reference-count that matters here. Reference-counts are only used to quickly determine what can be collected, most other methods just focus on the graph. The main problem is the reference from <code>a</code> to <code>a</code>.
The graph building functions basically build a tree. A node in the tree represents an object. Children of a node represent attributes of the object. Some of those attributes may have references to other objects, forming a subgraph.
The way to collect such an object is to delete all references to it, but all implementing algorithms must not alter the graph. As such, they simply flag objects that need to be collected, i.e. they mark nodes in the tree as collected

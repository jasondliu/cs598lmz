import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=None
lst

```

```python
import weakref
class Graph(object):pass
def callback(x):print x,x.data
class Node(object):pass
n1=Node()
n1.data='n1'
n2=Node()
n2.data='n2'
g=Graph()
g.root=n1
n1.graph=g
print 'Try to create a cycle...'
n1.parent=n2
n2.child=n1
print 'Try to break the cycle...'
n1.parent=None
print 'Try to create a cycle again...'
n1.child=n2
print 'Start referring to g...'
n1.graph.root=None
print 'End referring to g...'
n1.graph=None
```

## This chapter note

weak reference refers to an object but doesn't increase its reference count

the reference is automatically removed when the object is no longer needed

in python, weak reference are usually implemented in C

weak refernce are often

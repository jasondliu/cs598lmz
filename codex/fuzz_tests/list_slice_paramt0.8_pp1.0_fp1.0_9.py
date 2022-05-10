import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst
del a
</code>
The list is empty when it should have 1 element in it.


A:

<code>weakref</code>s are not suitable for cycle detection as is.
They prevent reachability through a reference but not through an attribute.
Here a and c are never reachable from the main program but from each other so the <code>weakref</code>s are cleared.
A <code>weakref</code> does not make an object unreachable, it only stops it from keeping a referent reachable.
You can use a <code>WeakKeyDictionary</code> to keep track of them though:
<code>import weakref

class A(object):
    pass

d={}

def callback(x):
    print(x)

a=A()
a.c=a
d[a]=1
keepalie=[]
keepalie.append(weakref.ref(a,callback))

del a
</code>
This will print the dictionary item when it is deleted:
<code>&lt;weakref at 0

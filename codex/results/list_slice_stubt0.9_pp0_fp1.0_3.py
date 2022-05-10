import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=weakref.ref(a,callback)
keepali0e.append(a)
keepali0e.append(a.b)
keepali0e.append(a.c)
del keepali0e[:]
print (len(lst))
</code>


A:

A <code>weakref</code> object is just an object like any other. Before you started deleting objects, you had 3 objects: an <code>A</code> object, an instance of <code>weakref</code> (which you hold a reference to in <code>a.b</code>), and <code>a</code> itself, which is referenced by <code>a.c</code>.
Now you're deleting them. When you delete <code>a</code>, <code>a.b</code>, and <code>a.c</code>, it breaks the cycle, so the <code>A</code> object gets deleted, which causes its last reference (the <code>weakref</code>) to stop existing, so that callback gets called and <code>del lst[0]</code

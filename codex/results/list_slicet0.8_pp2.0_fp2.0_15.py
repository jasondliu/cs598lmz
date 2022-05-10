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
You may also be interested in the source codes of <code>BDB</code> and <code>gdb</code>.
Related questions: How does python's garbage collector work?, what's the difference between circular reference and memory leak?


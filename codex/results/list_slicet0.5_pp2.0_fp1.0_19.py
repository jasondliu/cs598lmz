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
and it prints <code>1</code>, but I expected <code>2</code>.
I want to know what is the reason for this?


A:

I think this is because of the cyclic reference. <code>a</code> is referenced by the <code>lst</code> list, and <code>a</code> references itself. So the <code>a</code> object is not considered to be garbage-collectable.
You can test this by removing the <code>a.c = a</code> line.


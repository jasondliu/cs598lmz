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
print keepali0e
</code>
The output is:
<code>2
[['\x00\x00\x00\x00\x00\x00\x00\x00'], []]
</code>
The first list is the list of the weak reference.
The second list is the list of the objects that are still alive.


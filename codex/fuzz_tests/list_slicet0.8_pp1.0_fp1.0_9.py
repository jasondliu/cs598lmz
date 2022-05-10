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
print keepali0e
</code>
This code will make the list grow infinitely, because the first <code>str</code> object gets never removed from the list <code>keepali0e</code> (even if it would get de-referenced).


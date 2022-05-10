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
del keepali0e
</code>
The question is, what is the best way to do it?


A:

You can use the <code>gc.get_referrers</code> function:
<code>import gc

gc.get_referrers(some_object)
</code>
This will return a list of all objects that reference <code>some_object</code>.


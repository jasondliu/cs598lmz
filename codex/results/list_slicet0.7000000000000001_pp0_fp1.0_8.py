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
The <code>keepalive</code> list is a workaround for the fact that <code>a</code> is not kept alive by <code>lst</code> because it is stored as <code>str()</code> instead of <code>a</code>. The <code>keepalive</code> trick is used in similar situations in some of the answers to the question "What happen when a list changes size while iterating over it?"


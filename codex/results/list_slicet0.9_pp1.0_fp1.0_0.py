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
This is a little shorter, but it still works only if <code>lst[0] is not None</code>/<code>lst[0]</code> is a <code>str</code>.


import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
for i in range(2000000):lst.append(str())
</code>
Note that you must use the same reference in a callback as in the weakref. Otherwise, the first same reference of the gc'd object will be destroyed, and the second will be left in the indirect graph.


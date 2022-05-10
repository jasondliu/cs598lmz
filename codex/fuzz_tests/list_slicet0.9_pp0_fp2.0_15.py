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
There is, however, a way in a lot of cases to crash the interpreter by space running out, it's more of a hack and might not work on all systems, but here it is:
<code>import weakref
def callback(x):pass
lst=[str()]
keepali0e=[]
x={1:2}
keepali0e.append(weakref.ref(x,callback))
while lst:keepali0e.append([x[i] for i in range(len(x))])
del x
</code>
That latter one is O(n^2) with the size of the dictionary, so you want to use a small one.


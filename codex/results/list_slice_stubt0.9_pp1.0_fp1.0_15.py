import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
for i in range(100):lst.append(i*'hello')
</code>


A:

The problem is that the circular reference is preventing the weak reference from being collected.
Add a line before the second-to-last line to break the circular reference:
<code>a.c = None
del a
</code>


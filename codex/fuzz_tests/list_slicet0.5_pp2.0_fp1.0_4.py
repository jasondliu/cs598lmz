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
I'm trying to get this code to "leak" memory, but I can't seem to do it. Does anyone know how to get this to leak memory? I'm using Python 2.6.5. 


A:

Here's a way to get it to leak memory:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
while True:
    keepali0e=[]
    keepali0e.append(weakref.ref(a,callback))
    del a
</code>


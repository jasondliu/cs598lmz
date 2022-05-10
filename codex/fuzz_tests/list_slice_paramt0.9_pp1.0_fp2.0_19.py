import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e[0]()
keepali0e.pop()
lst.pop()
keepali0e.append(weakref.ref(lst,callback))
keepali0e.pop()
</code>
Above code is explained in the following blog:
<code>import weakref

class A(object):pass

def callback(x):del lst[0]

keepalive=[]

lst=[str()]

# b points to a
b=A()
b.c=b

keepalive.append(weakref.ref(b))
keepalive[0]()

keepalive.pop()

lst.pop()

# ref(...) add a reference cycle.
keepalive.append(weakref.ref(lst,callback))

keepalive.pop()
</code>
After running the above code, the memory of lst is not freed.
But when i modify the above code to:
<code>import weakref
class A(object):pass
def callback(x):del lst[0

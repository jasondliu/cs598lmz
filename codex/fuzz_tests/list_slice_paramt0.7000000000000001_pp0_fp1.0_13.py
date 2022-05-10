import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(a,callback))
del keepali0e
print(len(lst))
import weakref
class A(object):pass
class B(object):pass
def callback(x):print(x)
b=B()
b.c=b
a=A()
a.c=b
del a
callback=weakref.ref(a,callback)
del b
del a
del callback

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

#weakref.proxy(a)
#weakref.proxy(a,callback)
#weakref.proxy(a,callback,a)
#weakref.proxy(a,callback,a,a)
#weakref.proxy(a,callback,a,a,a)
#weakref.proxy(a,callback,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a,a,a,a,a)
#weakref.proxy(a,callback,a,a,a,a,a,a,a,a,a,a)
#weakref.proxy(a,callback,a,a

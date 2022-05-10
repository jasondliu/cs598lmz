import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(a))
print(keepali0e)
del a
print(keepali0e)
del lst
print(keepali0e)
#del keepali0e
print(keepali0e)

#weakref.ref(object,callback)
#weakref.proxy(object,callback)

#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keepali0e.append(weakref.ref(a,callback))
#keep

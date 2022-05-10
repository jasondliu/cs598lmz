import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst[0]=str()
keepali0e.append(weakref.ref(a,callback))
a.d=a
keepali0e.append(weakref.ref(a))
lst[0]=str()
del a
gc.collect()
print [r()for r in keepali0e]

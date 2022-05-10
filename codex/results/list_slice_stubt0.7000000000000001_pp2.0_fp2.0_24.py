import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.d)
weakref.ref(a,callback)
weakref.ref(a.c,callback)
weakref.ref(a.d,callback)
del a,a.c,a.d
gc.collect()
try:
    print (len(lst))
except TypeError:
    print ("TypeError")

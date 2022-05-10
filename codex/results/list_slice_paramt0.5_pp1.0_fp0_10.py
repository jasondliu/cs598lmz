import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
del a
gc.collect()
print len(lst)
print len(keepali0e)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
keepali0e.append(weakref.ref(a.c))
del a
gc.collect()
print len(lst)
print len(keepali0e)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
del a.c
gc.collect()
print len(lst)
print len(keepali0e)

def callback(x):del lst[0]
keepali0e=[]
lst

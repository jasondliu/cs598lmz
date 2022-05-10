import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(lst[1],callback))
keepali0e.append(weakref.ref(lst[1].c,callback))
del a,lst
print 'after deleting all references'
gc.collect()

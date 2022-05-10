import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a.c,callback))
del a
for i in range(2):
    print(lst,len(keepali0e))
    gc.collect()
#print(lst,len(keepali0e))
#gc.collect()

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(keepali0e[0])
del a
for i in range(6):
    print("%d elements need to be collected"%len(gc.collect()))
    time.sleep(1)
